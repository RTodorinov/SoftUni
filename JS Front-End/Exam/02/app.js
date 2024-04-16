window.addEventListener("load", solve);

function solve() {
    const addButtonElement = document.getElementById('add-btn');
    const nameInputElement = document.getElementById('name');
    const phoneInputElement = document.getElementById('phone');
    const categorySelectElement = document.getElementById('category');
    const checkListElement = document.getElementById('check-list');
    const contactListElement = document.getElementById('contact-list');

    addButtonElement.addEventListener('click', () => {
        const name = nameInputElement.value;
        const phone = phoneInputElement.value;
        const category = categorySelectElement.value;

        if (!name || !phone || !category) {
            return;
        }

        const contactLiElement = createContactElement(name, phone, category);
        checkListElement.appendChild(contactLiElement);

        nameInputElement.value = '';
        phoneInputElement.value = '';
        categorySelectElement.selectedIndex = 0;

        const editButtonElement = contactLiElement.querySelector('.edit-btn');
        editButtonElement.addEventListener('click', () => {
            nameInputElement.value = name;
            phoneInputElement.value = phone;
            categorySelectElement.value = category;

            contactLiElement.remove();
        });

        const saveButtonElement = contactLiElement.querySelector('.save-btn');
        saveButtonElement.addEventListener('click', () => {
            contactLiElement.remove();
            const newContactLiElement = createContactElement(nameInputElement.value, phoneInputElement.value, categorySelectElement.value);
            contactListElement.appendChild(newContactLiElement);
        });
    });

    function createContactElement(name, phone, category) {
        const namePEl = document.createElement('p');
        namePEl.textContent = `name: ${name}`;

        const phonePEl = document.createElement('p');
        phonePEl.textContent = `phone: ${phone}`;

        const categoryPEl = document.createElement('p');
        categoryPEl.textContent = `category: ${category}`;

        const articleEl = document.createElement('article');
        articleEl.appendChild(namePEl);
        articleEl.appendChild(phonePEl);
        articleEl.appendChild(categoryPEl);

        const editBtn = document.createElement('button');
        editBtn.classList.add('edit-btn');
        editBtn.textContent = 'Edit';

        const saveBtn = document.createElement('button');
        saveBtn.classList.add('save-btn');
        saveBtn.textContent = 'Save';

        const buttonsDiv = document.createElement('div');
        buttonsDiv.classList.add('buttons');
        buttonsDiv.appendChild(editBtn);
        buttonsDiv.appendChild(saveBtn);

        const contactLiEl = document.createElement('li');
        contactLiEl.appendChild(articleEl);
        contactLiEl.appendChild(buttonsDiv);

        return contactLiEl;
    }
}

