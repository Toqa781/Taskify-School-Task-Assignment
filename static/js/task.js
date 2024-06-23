// delete
document.addEventListener('DOMContentLoaded', function() {
    const taskItems = document.querySelectorAll('.container ul li');

    function deleteTask(taskId) {
        if (confirm("Are you sure you want to delete this task?")) {
            fetch(`/delete_task/${taskId}/`, {
                method: 'DELETE',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCsrfToken(),
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    const taskElement = document.getElementById(`task-${taskId}`);
                    taskElement.remove();
                } else {
                    alert('Failed to delete task.');
                }
            })
            .catch(error => console.error('Error:', error));
        }
    }

    function getCsrfToken() {
        return document.querySelector('[name=csrfmiddlewaretoken]').value;
    }

    taskItems.forEach(function(taskItem) {
        taskItem.querySelector('button').addEventListener('click', function() {
            const taskId = this.getAttribute('data-task-id');
            deleteTask(taskId);
        });
    });
});
// edit
const editTask = () => {
    window.location.href = "Edit.html";
};

document.querySelector('a[href="Edit.html"] button').addEventListener('click', function(event) {
    if (!editTask()) {
        event.preventDefault(); 
    }
});
document.getElementById("res").innerHTML=localStorage.getItem("TtitleVal");
document.getElementById("res1").innerHTML=localStorage.getItem("taskidVal");
document.getElementById("res2").innerHTML=localStorage.getItem("TtitleVal");
document.getElementById("res3").innerHTML=localStorage.getItem("teacherN");
document.getElementById("res4").innerHTML=localStorage.getItem("des");
document.getElementById("res5").innerHTML=localStorage.getItem("adimnN");
document.getElementById("res6").innerHTML=localStorage.getItem("option");