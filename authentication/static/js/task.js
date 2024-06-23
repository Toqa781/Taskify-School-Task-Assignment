

// delete
const deleteTask = () => {
    if (confirm("Are you sure you want to delete this task?")) {
        window.location.href = "empty.html";
    }
};

document.querySelector('a[href="AdminHome.html"] button').addEventListener('click', function(event) {
    if (!deleteTask()) {
        event.preventDefault(); 
    }
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