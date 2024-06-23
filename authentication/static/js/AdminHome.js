var x = document.getElementById("upcom");
var y = document.getElementById("ovrdu");
var z = document.getElementById("cmplt");
        function upcoming() {
            x.style.left = "15px";
            y.style.left = "900px";
            z.style.left = "1200px";
        }

        function overdue() {
            x.style.left = "-1185px";
            y.style.left = "15px";
            z.style.left = "900px"
        }
        function completed() {
            x.style.left = "-2090px";
            y.style.left = "-900px";
            z.style.left="15px"
        }
        document.getElementById("id").innerHTML=localStorage.getItem("TtitleVal");
        document.getElementById("user").innerHTML=localStorage.getItem("username");