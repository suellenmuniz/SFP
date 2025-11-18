// Alternância visual
const card = document.getElementById("card");
const btnCadastro = document.getElementById("btnCadastro");
const btnLogin = document.getElementById("btnLogin");

btnCadastro.addEventListener("click", () => card.classList.add("active"));
btnLogin.addEventListener("click", () => card.classList.remove("active"));


// Abrir automaticamente a aba correta quando o Flask manda abrir=cadastro
const params = new URLSearchParams(window.location.search);
if (params.get("abrir") === "cadastro") {
  card.classList.add("active");
}


// mostrar/ocultar senha

function toggleSenha(buttonId, inputId) {
  const btn = document.getElementById(buttonId);
  const input = document.getElementById(inputId);
  if (!btn || !input) return;

  btn.addEventListener("click", () => {
    if (input.type === "password") {
      input.type = "text";
      btn.textContent = "Ocultar";
    } else {
      input.type = "password";
      btn.textContent = "Mostrar";
    }
  });
}

toggleSenha("toggleLoginSenha", "loginSenha");
toggleSenha("toggleCadSenha", "cadSenha");
toggleSenha("toggleCadConfirmar", "cadConfirma");




