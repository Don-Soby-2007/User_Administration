// JavaScript for handling Create User Modal

function openCreateUser(){
    var m = document.getElementById('createUserModal');
    if (m) { m.classList.add('open'); }
}

function closeCreateUser(){
    var m = document.getElementById('createUserModal');
    if (m) { m.classList.remove('open'); }
}

// Handle form submission for creating a new user

document.getElementById('createUserForm').addEventListener('submit', function(e) {
  e.preventDefault();

  const form = this;
  const errorDiv = document.getElementById('errorMessage');
  const formData = new FormData(form);

  // Simple frontend check
  if (formData.get('password') !== formData.get('confirm_password')) {
    errorDiv.textContent = "Passwords do not match.";
    errorDiv.style.display = 'block';
    return;
  }

  fetch(createUserUrl, {
    method: 'POST',
    headers: {
      'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
    },
    body: formData
  })
  .then(response => response.json())
  .then(data => {
    if (data.success) {
        
      //  User created successfully

      form.reset();
      errorDiv.style.display = 'none';
      closeCreateUser();
      alert("User created successfully!");
      location.reload();  

    } else {
      // Show error message
      errorDiv.textContent = data.message || "Something went wrong!";
      errorDiv.style.display = 'block';
    }
  })
  .catch(() => {
    errorDiv.textContent = "Server error. Please try again.";
    errorDiv.style.display = 'block';
  });
});


