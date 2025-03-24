document.getElementById("registerForm").addEventListener("submit", function (event) {
    if (!document.getElementById("name").value || 
        !document.getElementById("email").value || 
        !document.getElementById("password").value) {
        alert("All fields are required!");
        event.preventDefault();
    }
});
