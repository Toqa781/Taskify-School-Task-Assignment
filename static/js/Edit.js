document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");

    // Function to show error messages
    function showError(errorElement, errorMessage) {
        const error = document.querySelector("." + errorElement);
        error.classList.add("display-error");
        error.innerHTML = errorMessage;
    }

    // Function to clear error messages
    function clearError() {
        const errors = document.querySelectorAll(".error");
        errors.forEach(error => {
            error.innerHTML = "";
            error.classList.remove("display-error");
        });
    }

    // Function to handle form submission
    function handleSubmit(event) {
        event.preventDefault(); // Prevent default form submission
        clearError(); // Clear previous errors before validation

        const tasktitle = document.getElementById("tasktitle");
        const teachername = document.getElementById("teachername");
        const description = document.getElementById("description");
        const createdby = document.getElementById("createdby");

        let isValid = true;

        if (tasktitle.value === "") {
            showError("title-error", "Invalid Task Title, it cannot be empty.");
            isValid = false;
        } else if (tasktitle.value.length > 55) {
            showError("title-error", "Invalid Task Title, it cannot be greater than 55 characters.");
            isValid = false;
        }

        if (teachername.value === "") {
            showError("TName-error", "Invalid Teacher Name, it cannot be empty.");
            isValid = false;
        } else if (teachername.value.length > 55) {
            showError("TName-error", "Invalid, it cannot be greater than 55 characters.");
            isValid = false;
        }

        if (description.value.length > 160) {
            showError("des-error", "Invalid Description, it cannot be greater than 160 characters.");
            isValid = false;
        }

        if (createdby.value === "") {
            showError("admin-error", "Invalid admin name, it cannot be empty.");
            isValid = false;
        }

        if (isValid) {
            // Perform AJAX form submission
            let formData = new FormData(form);
            let url = form.action;

            fetch(url, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-Requested-With': 'XMLHttpRequest'
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert(data.message);
                    // Optionally redirect or update the page
                    window.location.href = `/tasks/${task_id}/`;
                } else {
                    let errors = data.errors;
                    for (let field in errors) {
                        showError(field + '-error', errors[field][0]);
                    }
                }
            })
            .catch(error => console.error('Error:', error));
        }
    }

    // Attach event listener to form submission
    form.addEventListener("submit", handleSubmit);
});
