$(document).ready(function() {
	let validInputs = [];

	function isValidEmail(email) {
		var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
		return regex.test(email);
	}

	function validate() {
		const isValid = ['first_name', 'email', 'username', 'password'].every(item => {
			return validInputs.indexOf(item) >= 0;
		});
		if (isValid) {
			$('#register_submit_btn').removeAttr('disabled');
		} else {
			$('#register_submit_btn').attr('disabled', 'disabled');
		}
	}

	function checkStrength(password) {
		var strength = 0;

		if (password.length < 6) {
			$('#div_password')
				.removeClass('has-success')
				.removeClass('has-warning')
				.addClass('has-error');
			return 'Password too short';
		}

		if (password.length > 7) strength += 1;
		if (password.match(/([a-z].*[A-Z])|([A-Z].*[a-z])/)) strength += 1;
		if (password.match(/([a-zA-Z])/) && password.match(/([0-9])/)) strength += 1;
		if (password.match(/([!,%,&,@,#,$,^,*,?,_,~])/)) strength += 1;
		if (password.match(/(.*[!,%,&,@,#,$,^,*,?,_,~].*[!,",%,&,@,#,$,^,*,?,_,~])/)) strength += 1;

		if (strength < 2) {
			$('#div_password')
				.removeClass('has-success')
				.removeClass('has-warning')
				.addClass('has-error');
			return 'Password weak';
		} else if (strength == 2) {
			$('#div_password')
				.removeClass('has-error')
				.removeClass('has-success')
				.addClass('has-warning');
			return 'Good';
		} else {
			$('#div_password')
				.removeClass('error')
				.removeClass('has-error')
				.removeClass('has-warning')
				.addClass('has-success');
			return 'Strong';
		}
	}

	function validateFirstName() {
		const firstName = $('#register_first_name').val();
		if (firstName && firstName.trim().length > 0) {
			if (validInputs.indexOf('first_name') === -1) validInputs.push('first_name');
			$('#div_first_name').removeClass('has-error').addClass('has-success');
		} else {
			validInputs = validInputs.filter(item => item !== 'first_name');
			if (firstName !== undefined && firstName.length > 0) {
				$('#div_first_name').removeClass('has-success').addClass('has-error');
			}
		}
		validate();
	}

	function validateUsername() {
		const username = $('#register_username').val();
		$('#usernameHelpBlock').addClass('hikaya-hide');
		if (username && username.trim().length > 0) {
			if (validInputs.indexOf('username') === -1) validInputs.push('username');
			$('#div_username').removeClass('has-error').addClass('has-success');
		} else {
			validInputs = validInputs.filter(item => item !== 'username');
			if (username !== undefined && username.length > 0) {
				$('#div_username').removeClass('has-success').addClass('has-error');
			}
		}
		validate();
	}

	function validateEmail() {
		const emailAddress = $('#register_email_address').val();
		if (emailAddress && isValidEmail(emailAddress)) {
			if (validInputs.indexOf('email') === -1) validInputs.push('email');
			$('#div_email_address').removeClass('has-error').addClass('has-success');
			$('#emailHelpBlock').removeClass('hikaya-show').addClass('hikaya-hide');
		} else {
			validInputs = validInputs.filter(item => item !== 'email');
			if (emailAddress && emailAddress.length > 0) {
				$('#div_email_address').removeClass('has-success').addClass('has-error');
				$('#emailHelpBlock').removeClass('hikaya-hide').addClass('hikaya-show');
			}
		}
		validate();
	}

	function validatePasswords() {
		const password = $('#register_password').val() || '';
		const confirmPassword = $('#register_confirm_password').val() || '';

		if (password.length > 0) {
			$('#passwordHelpBlock').html(checkStrength(password));
		} else {
			$('#passwordHelpBlock').html('');
			$('#div_password').removeClass('has-success has-warning has-error');
		}

		if (confirmPassword.length > 0 || password.length > 0) {
			if (password.length >= 6 && confirmPassword === password) {
				if (validInputs.indexOf('password') === -1) validInputs.push('password');
				$('#div_confirm_password').removeClass('has-error').addClass('has-success');
				$('#confirmPasswordHelpBlock').addClass('hikaya-hide').html('');
			} else {
				validInputs = validInputs.filter(item => item !== 'password');
				if (confirmPassword.length > 0) {
					$('#div_confirm_password').removeClass('has-success').addClass('has-error');
					$('#confirmPasswordHelpBlock').removeClass('hikaya-hide').html('Passwords do not match');
				}
			}
		} else {
			validInputs = validInputs.filter(item => item !== 'password');
			$('#div_confirm_password').removeClass('has-success has-error');
			$('#confirmPasswordHelpBlock').addClass('hikaya-hide').html('');
		}
		validate();
	}

	// Attach event handlers
	$('#register_first_name').on('input focus keyup change', validateFirstName);
	$('#register_username').on('input focus keyup change', validateUsername);
	$('#register_email_address').on('input focus keyup change', validateEmail);
	$('#register_password').on('input focus keyup change', validatePasswords);
	$('#register_confirm_password').on('input focus keyup change', validatePasswords);

	// Check initial values
	validateFirstName();
	validateUsername();
	validateEmail();
	validatePasswords();
});
