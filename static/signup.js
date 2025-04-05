document.getElementById("signUpForm").addEventListener("submit",function(e){
let password=document.getElementById("password")
let Cpassword=document.getElementById("Cpassword")
let error=document.getElementById("errorMessage")

if(password.value!==Cpassword.value){
    error.innerText="Password does not matched"
    password.value=""
    Cpassword.value=""
    e.preventDefault()

}
else{
    error.innerText=""
}
});