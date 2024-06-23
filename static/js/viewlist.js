document.addEventListener('DOMContentLoaded', function() {
    const taskListItems = document.querySelectorAll('#task-list li');

    taskListItems.forEach(item => {
        item.addEventListener('click', function() {
            taskListItems.forEach(li => li.classList.remove('selected'));
            this.classList.add('selected');
        });
    });
});
