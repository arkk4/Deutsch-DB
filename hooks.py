# hooks.py
import os
import frontmatter
import jinja2

def generate_dictionary_pages(config, **kwargs):
    """
    Хук on_pre_build: рендерить raw/*.md через Jinja і пише
    docs/dictionary/<slug>.md до того, як MkDocs збиратиме сайт.
    
    Обробляє лише ті файли, які були змінені з моменту останньої генерації,
    або для яких ще не існує згенерованої сторінки.
    """
    docs_dir = config['docs_dir']
    project_base_dir = os.path.dirname(docs_dir)
    raw_dir = os.path.join(project_base_dir, 'sources', 'dictionary', 'raw')
    tmpl_dir = os.path.join(project_base_dir, 'sources', 'dictionary', 'page_templates')
    
    # Перевіряємо чи існують потрібні директорії
    if not os.path.exists(raw_dir):
        print(f"⚠️  Директорія {raw_dir} не існує")
        return
    if not os.path.exists(tmpl_dir):
        print(f"⚠️  Директорія {tmpl_dir} не існує")
        return
    
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(tmpl_dir),
        autoescape=False,
        trim_blocks=True,
        lstrip_blocks=True
    )
    
    print("ℹ️  Починаємо генерацію сторінок словника...")
    for fname in sorted(os.listdir(raw_dir)):
        if not fname.endswith('.md'):
            continue
            
        slug = fname[:-3]
        source_path = os.path.join(raw_dir, fname)
        out_path = os.path.join(docs_dir, 'dictionary', f"{slug}.md")

        # --- ЗМІНЕНО ---
        # Перевіряємо, чи існує вихідний файл і чи він новіший за сирий файл.
        # Якщо так, пропускаємо генерацію, щоб зекономити час.
        if os.path.exists(out_path):
            # Отримуємо час останньої модифікації для обох файлів
            source_mtime = os.path.getmtime(source_path)
            dest_mtime = os.path.getmtime(out_path)
            
            # Якщо сирий файл не новіший за згенерований, пропускаємо його
            if source_mtime <= dest_mtime:
                # Ви можете розкоментувати наступний рядок для більш детального логування
                # print(f"⏭️  Пропущено (не змінено): dictionary/{slug}.md")
                continue
        # --- КІНЕЦЬ ЗМІН ---
        
        try:
            post = frontmatter.load(source_path)
            meta = post.metadata
            part = meta.get('part_of_speech', 'andere')
            tmpl_name = f"{part}.md"
            
            if not os.path.exists(os.path.join(tmpl_dir, tmpl_name)):
                tmpl_name = "andere.md"
            
            tmpl = env.get_template(tmpl_name)
            content = tmpl.render(meta=meta)
            
            with open(out_path, 'w', encoding='utf-8') as f:
                f.write(content)
                
            print(f"🛠️  Згенеровано: dictionary/{slug}.md")
        except Exception as e:
            print(f"❌ Помилка при обробці {fname}: {e}")
            continue
            
    print("✅ Генерацію сторінок словника завершено.")