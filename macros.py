# macros.py
import os
import frontmatter
import yaml
import re

def define_env(env):
    def _get_template_structure(template_dir):
        """Парсить шаблони і витягує структуру frontmatter"""
        template_structures = {}
        
        if not os.path.exists(template_dir):
            return template_structures
            
        for template_file in os.listdir(template_dir):
            if not template_file.endswith('.md'):
                continue
                
            template_name = template_file[:-3]  # видаляємо .md
            template_path = os.path.join(template_dir, template_file)
            
            try:
                with open(template_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Шукаємо frontmatter в шаблоні
                if content.startswith('---'):
                    # Витягуємо frontmatter з шаблону
                    frontmatter_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
                    if frontmatter_match:
                        frontmatter_content = frontmatter_match.group(1)
                        
                        # Парсимо YAML, але ігноруємо Jinja змінні
                        try:
                            # Замінюємо Jinja змінні на пусті рядки для парсингу структури
                            cleaned_content = re.sub(r'\{\{.*?\}\}', '""', frontmatter_content)
                            structure = yaml.safe_load(cleaned_content)
                            
                            if structure:
                                template_structures[template_name] = structure
                        except yaml.YAMLError:
                            # Якщо не можемо парсити YAML, створюємо базову структуру
                            template_structures[template_name] = {
                                'title': '',
                                'translate': '',
                                'part_of_speech': template_name
                            }
                            
            except Exception as e:
                print(f"Помилка при обробці шаблону {template_file}: {e}")
                continue
                
        return template_structures
    
    def _extract_fields_from_term(meta, template_structure):
        """Витягує поля з терміна відповідно до структури шаблону"""
        result = {}
        
        for field_name, default_value in template_structure.items():
            if field_name in meta:
                result[field_name] = meta[field_name]
            else:
                result[field_name] = default_value
                
        return result
    
    @env.macro
    def terms():
        project_base_dir = os.path.dirname(env.conf['docs_dir'])
        template_dir = os.path.join(project_base_dir, 'sources', 'dictionary', 'schema_templates')
        base = os.path.join(env.conf['docs_dir'], 'dictionary')
        items = []
        
        # Перевіряємо чи існує директорія
        if not os.path.exists(base):
            return items
        
        # Отримуємо структури шаблонів
        template_structures = _get_template_structure(template_dir)
        
        for name in sorted(os.listdir(base)):
            if not name.endswith('.md') or name == 'index.md':
                continue
                
            slug = name[:-3]
            file_path = os.path.join(base, name)
            
            try:
                post = frontmatter.load(file_path)
                meta = post.metadata
                part_of_speech = meta.get('part_of_speech', 'andere')
                
                # Використовуємо структуру відповідного шаблону
                template_structure = template_structures.get(part_of_speech, {
                    'title': '',
                    'translate': '',
                    'part_of_speech': part_of_speech
                })
                
                term_data = _extract_fields_from_term(meta, template_structure)
                term_data["slug"] = slug
                term_data["url"] = f"/dictionary/{slug}/"
                
                items.append(term_data)
            except Exception as e:
                print(f"Помилка при обробці {file_path}: {e}")
                continue
                
        return items
    
    @env.macro
    def terms_by_part_of_speech():
        """Групує терміни за part_of_speech"""
        all_terms = terms()
        grouped = {}
        
        for term in all_terms:
            pos = term.get('part_of_speech', 'andere')
            if pos not in grouped:
                grouped[pos] = []
            grouped[pos].append(term)
            
        return grouped
    
    @env.macro
    def get_part_of_speech_display_name(pos):
        """Повертає локалізовану назву для part_of_speech"""
        names = {
            'verb': 'Дієслова',
            'nomen': 'Іменники',
            'adjective': 'Прикметники',
            'preposition': 'Прийменники',
            'adverb': 'Прислівники',
            'conjunction': 'Сполучники',
            'particle': 'Частки',
            'andere': 'Інше'
        }
        return names.get(pos, pos.capitalize())
    
    @env.macro
    def get_template_fields(part_of_speech):
        """Повертає поля для конкретного part_of_speech на основі шаблону"""
        project_base_dir = os.path.dirname(env.conf['docs_dir'])
        template_dir = os.path.join(project_base_dir, 'sources', 'dictionary', 'schema_templates')
        template_structures = _get_template_structure(template_dir)
        return template_structures.get(part_of_speech, {})