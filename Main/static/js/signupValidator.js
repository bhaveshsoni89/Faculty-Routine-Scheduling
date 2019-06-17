
  // polyfill for RegExp.escape
  if(!RegExp.escape) {
    RegExp.escape = function(s) {
      return String(s).replace(/[\\^$*+?.()|[\]{}]/g, '\\$&');
    };
  }

  document.addEventListener("DOMContentLoaded", function() {

    // JavaScript form validation


    var checkForm = function checkForm(signForm)
    {

      var name = document.getElementById('Name').value;
        if (name == '')
        {

        }
      if(signForm.email.value == "")
      {
        alert("Error: Email can not be blank!");
        this.email.focus();
        e.preventDefault(); // equivalent to return false
        return;
      }
      var re = /^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$/;
      if(!re.test(this.email.value))
      {
        alert("Error: Email must be valid Email id !");
        this.email.focus();
        e.preventDefault();
        return;
      }




      reg = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,}$/;
      if(this.password.value != "" && this.password.value == this.confirm.value)
      {
        if(!reg.test(this.password.value))
        {
          alert("The password you have entered is not valid!");
          this.password.focus();
          e.preventDefault();
          return false;
        }
      }
       else
       {
        alert("Error: Please check that you've entered and confirmed your password!");
        this.password.focus();
        e.preventDefault();
        return false;
      }




    };

    var signForm = document.getElementById("signForm");
    signForm.addEventListener("submit", checkForm, true);

    // HTML5 form validation

    var supports_input_validity = function()
    {
      var i = document.createElement("input");
      return "setCustomValidity" in i;
    };

    if(supports_input_validity()) {
      var EmailInput = document.getElementById("email");
      EmailInput.setCustomValidity(EmailInput.title);

      var PasswordInput = document.getElementById("password");
      PasswordInput.setCustomValidity(PasswordInput.title);

      var ConfirmInput = document.getElementById("confirm");

      // input key handlers

      EmailInput.addEventListener("keyup", function(e) {
        EmailInput.setCustomValidity(this.validity.patternMismatch ? EmailInput.title : "");
      }, false);

      PasswordInput.addEventListener("keyup", function(e) {
        this.setCustomValidity(this.validity.patternMismatch ? PasswordInput.title : "");
        if(this.checkValidity()) {
          ConfirmInput.pattern = RegExp.escape(this.value);
          ConfirmInput.setCustomValidity(ConfirmInput.title);
        } else {
          ConfirmInput.pattern = this.pattern;
          ConfirmInput.setCustomValidity("");
        }
      }, false);

      ConfirmInput.addEventListener("keyup", function(e) {
        this.setCustomValidity(this.validity.patternMismatch ? ConfirmInput.title : "");
      }, false);

    }

  }, false);

