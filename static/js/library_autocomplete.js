// static/js/library_autocomplete.js
document.addEventListener("DOMContentLoaded", function() {
    const input = document.querySelector('input[list="existing_books"]');
    if (!input) return;

    const datalist = document.createElement('datalist');
    datalist.id = 'existing_books';
    input.parentNode.appendChild(datalist);

    fetch('/api/books/')  // یک API کوچک که تمام کتاب‌ها رو برمی‌گردونه
        .then(res => res.json())
        .then(data => {
            data.forEach(book => {
                const option = document.createElement('option');
                option.value = book.name;
                datalist.appendChild(option);
            });
        });
});