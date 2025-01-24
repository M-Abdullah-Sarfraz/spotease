document.getElementById('signupForm').addEventListener('submit', async function(event) {
    event.preventDefault();

    const formData = {
        first_name: document.querySelector('input[name="first_name"]').value,
        last_name: document.querySelector('input[name="last_name"]').value,
        email: document.querySelector('input[name="email"]').value,
        password: document.querySelector('input[name="password"]').value,
        username: document.querySelector('input[name="email"]').value,  // Username same as email
    };

    try {
        const response = await fetch('/api/accounts/signup/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(formData)
        });

        if (response.ok) {
            alert('Signup successful! Please login.');
            window.location.href = '/admin/';
        } else {
            alert('Signup failed. Please try again.');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('Something went wrong. Try again later.');
    }
});
