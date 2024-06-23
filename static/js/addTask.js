
let Ttitle = document.querySelector("[name='title']");
let teacherN = document.querySelector("[name='teacher']");
let des = document.querySelector("[name='Description']");
let admin = document.querySelector("[name='admin']");
let priority = document.querySelector("[name='choose']");

// Function to show error messages
function showError(errorElement, errorMessage) {
    document.querySelector("." + errorElement).classList.add("dispaly-error");
    document.querySelector("." + errorElement).innerHTML = errorMessage;
}

// Function to clear all error messages
function clearError() {
    let errors = document.querySelectorAll(".error");
    for (let error of errors) {
        error.innerHTML = "";
        error.classList.remove("dispaly-error");
    }
}

// Form submission validation
document.forms[0].onsubmit = function(event) {
    clearError();
    
    let isValid = true;

    // Validate Task Title
    if (Ttitle.value.trim() === "") {
        showError("title-error", "Invalid Task Title, it cannot be empty.");
        isValid = false;
    } else if (Ttitle.value.length > 55) {
        showError("title-error", "Invalid Task Title, it cannot be greater than 55 characters.");
        isValid = false;
    }

    // Validate Teacher Name
    if (teacherN.value.trim() === "") {
        showError("TName-error", "Invalid Teacher Name, it cannot be empty.");
        isValid = false;
    } else if (teacherN.value.length > 55) {
        showError("TName-error", "Invalid, it cannot be greater than 55 characters.");
        isValid = false;
    }

    // Validate Description
    if (des.value.length > 160) {
        showError("des-error", "Invalid Description, it cannot be greater than 160 characters.");
        isValid = false;
    }

    // Validate Admin (optional, since it's usually populated and disabled)
    if (admin.value.trim() === "") {
        showError("admin-error", "Invalid admin name, it cannot be empty.");
        isValid = false;
    }

    // Validate Priority
    if (!priority.value) {
        showError("priority-error", "Please select a priority.");
        isValid = false;
    }

    // Prevent form submission if not valid
    if (!isValid) {
        event.preventDefault();
    } else {
        // Reset the fields after submission if desired (usually, this is handled by the server response)
        Ttitle.value = "";
        teacherN.value = "";
        des.value = "";
        priority.value = "";
        // admin.value = ""; // this is usually not needed as it's a disabled field
    }
};
