
    const username = localStorage.getItem('userToken');
    const currentUser = document.getElementById("username");
    currentUser.innerText = username;

    function checkLocalSession() {
      if (!username) {
        // Redirect to login page if no username is found
        window.location.href = "./pages/auth/login.html";
      }
    }

    function logout() {
      localStorage.clear();
      window.location.href = "./pages/auth/login.html";
    }

    checkLocalSession();
