// docs/overrides/extra.js
document.addEventListener('DOMContentLoaded', function() {
    const cardWrappers = document.querySelectorAll('.card-wrapper[data-url]');
    cardWrappers.forEach(wrapper => {
        wrapper.addEventListener('click', function() {
            window.location.href = this.dataset.url;
        });
    });
});