// function validatePasswordMatch() {
//     const password = document.getElementById('password').value;
//     const confirmPassword = document.getElementById('confirm-password').value;
    
//     if (password !== confirmPassword) {
//         return false;
//     }
//     return true;
// }

// // Function to show error message
// function showErrorMessage(message) {
//     // Remove existing error message if any
//     const existingError = document.querySelector('.password-error');
//     if (existingError) {
//         existingError.remove();
//     }
    
//     // Create error message element
//     const errorDiv = document.createElement('div');
//     errorDiv.className = 'password-error';
//     errorDiv.textContent = message;
    
//     // Insert error message before the submit button
//     const submitButton = document.querySelector('.btn-register');
//     submitButton.parentNode.insertBefore(errorDiv, submitButton);
// }

// // Function to remove error message
// function removeErrorMessage() {
//     const errorMessage = document.querySelector('.password-error');
//     if (errorMessage) {
//         errorMessage.remove();
//     }
// }

// // Wait for DOM to be fully loaded
// document.addEventListener('DOMContentLoaded', function() {
//     const signupForm = document.querySelector('.login-form');
    
//     if (signupForm) {
//         // Add event listener for form submission
//         signupForm.addEventListener('submit', function(event) {
//             event.preventDefault(); // Prevent default form submission
            
//             // Check if passwords match
//             if (!validatePasswordMatch()) {
//                 showErrorMessage('Passwords do not match. Please try again.');
//                 return false;
//             }
            
//             // Remove error message if passwords match
//             removeErrorMessage();
            
//             // If passwords match, form can be submitted
//             // You can add additional logic here, like sending data to server
//             alert('Form submitted successfully! Passwords match.');
//             // Uncomment the line below to actually submit the form
//             // signupForm.submit();
//         });
        
//         // Optional: Real-time validation feedback while typing
//         const confirmPasswordInput = document.getElementById('confirm-password');
//         if (confirmPasswordInput) {
//             const confirmPasswordGroup = confirmPasswordInput.closest('.input-group');
            
//             confirmPasswordInput.addEventListener('input', function() {
//                 const password = document.getElementById('password').value;
//                 const confirmPassword = this.value;
                
//                 if (confirmPassword.length > 0) {
//                     if (password !== confirmPassword) {
//                         // Add visual feedback for mismatch (red border)
//                         confirmPasswordGroup.style.boxShadow = '0 0 0 2px rgba(255, 107, 107, 0.5)';
//                         confirmPasswordGroup.style.borderColor = '#ff6b6b';
//                     } else {
//                         // Add visual feedback for match (green border)
//                         confirmPasswordGroup.style.boxShadow = '0 0 0 2px rgba(77, 192, 181, 0.5)';
//                         confirmPasswordGroup.style.borderColor = '#4dc0b5';
//                         removeErrorMessage();
//                     }
//                 } else {
//                     // Reset border when field is empty
//                     confirmPasswordGroup.style.boxShadow = '';
//                     confirmPasswordGroup.style.borderColor = '';
//                 }
//             });
            
//             // Also check on password field change
//             const passwordInput = document.getElementById('password');
//             if (passwordInput) {
//                 passwordInput.addEventListener('input', function() {
//                     const confirmPassword = document.getElementById('confirm-password').value;
//                     if (confirmPassword.length > 0) {
//                         if (this.value !== confirmPassword) {
//                             confirmPasswordGroup.style.boxShadow = '0 0 0 2px rgba(255, 107, 107, 0.5)';
//                             confirmPasswordGroup.style.borderColor = '#ff6b6b';
//                         } else {
//                             confirmPasswordGroup.style.boxShadow = '0 0 0 2px rgba(77, 192, 181, 0.5)';
//                             confirmPasswordGroup.style.borderColor = '#4dc0b5';
//                             removeErrorMessage();
//                         }
//                     } else {
//                         confirmPasswordGroup.style.boxShadow = '';
//                         confirmPasswordGroup.style.borderColor = '';
//                     }
//                 });
//             }
//         }
//     }
// });
