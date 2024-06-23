// Get the markAsDoneBtn and add event listener
document.getElementById('markAsDoneBtn').addEventListener('click', function() {
    // Get the task ID from the data attribute
    const taskId = this.getAttribute('data-task-id');
    console.log(taskId)
    // Make the fetch request with the correct URL
    fetch(`/task/${taskId}/mark_as_done/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': '{{ csrf_token }}',  // Ensure CSRF token is included for security
        },
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            alert('Task marked as done');
            window.location.href = 'http://127.0.0.1:8000/completed/';
        } else {
            alert('Failed to update task status');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred while updating the task status');
    });
});

document.getElementById('cancelBtn').addEventListener('click', function() {
    window.history.back();
});
