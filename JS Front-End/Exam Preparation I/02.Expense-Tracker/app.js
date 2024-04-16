window.addEventListener("load", solve);

function solve() {
    const expenseForm = document.querySelector('.expense-content');
    const addBtn = document.getElementById('add-btn');
    const previewList = document.getElementById('preview-list');
    const expensesList = document.getElementById('expenses-list');
    
    // Function to add item to preview list
    function addToPreviewList(expenseType, amount, date) {
        // Create new preview item
        const newPreviewItem = document.createElement('li');
        newPreviewItem.textContent = `${expenseType}: $${amount} (${date})`;

        // Append item to preview list
        previewList.appendChild(newPreviewItem);

        // Disable add button
        addBtn.disabled = true;

        // Clear form inputs
        expenseForm.reset();

        // Event listener for edit button
        const editBtn = document.createElement('button');
        editBtn.textContent = 'Edit';
        editBtn.classList.add('edit-btn');
        newPreviewItem.appendChild(editBtn);
        editBtn.addEventListener('click', function() {
            // Set form values
            const info = newPreviewItem.textContent.split(': ')[1].split(' (');
            document.getElementById('expense').value = info[0];
            document.getElementById('amount').value = parseFloat(info[1].split(')')[0]);
            document.getElementById('date').value = info[2].split(')')[0];

            // Remove item from preview list
            previewList.removeChild(newPreviewItem);

            // Enable add button
            addBtn.disabled = false;
        });

        // Event listener for delete button
        const deleteBtn = document.createElement('button');
        deleteBtn.textContent = 'Delete';
        deleteBtn.classList.add('delete-btn');
        newPreviewItem.appendChild(deleteBtn);
        deleteBtn.addEventListener('click', function() {
            // Remove item from preview list
            previewList.removeChild(newPreviewItem);

            // Enable add button
            addBtn.disabled = false;
        });
    }

    // Event listener for add button
    addBtn.addEventListener('click', function(event) {
        event.preventDefault(); // Prevent default form submission behavior

        // Get form values
        const expenseType = document.getElementById('expense').value.trim();
        const amount = parseFloat(document.getElementById('amount').value);
        const date = document.getElementById('date').value.trim();

        // Validate inputs
        if (expenseType === '' || isNaN(amount) || amount <= 0 || date === '') {
            alert('Please fill out all fields correctly.');
            return;
        }

        // Add item to preview list
        addToPreviewList(expenseType, amount, date);
    });

    // Event listener for Ok button
    document.getElementById('main').addEventListener('click', function(event) {
        if (event.target.classList.contains('ok-btn')) {
            const listItem = event.target.parentElement;
            listItem.removeChild(event.target.previousElementSibling); // Remove edit button
            listItem.removeChild(event.target); // Remove Ok button
            expensesList.appendChild(listItem); // Move item to expenses list
            addBtn.disabled = false; // Enable add button
        }
    });

    // Event listener for delete button
    document.getElementById('main').addEventListener('click', function(event) {
        if (event.target.classList.contains('delete-btn')) {
            window.location.reload(); // Reload the application
        }
    });
}
