// Alternância visual
const card = document.getElementById("card");
const btnCadastro = document.getElementById("btnCadastro");
const btnLogin = document.getElementById("btnLogin");

btnCadastro.addEventListener("click", () => card.classList.add("active"));
btnLogin.addEventListener("click", () => card.classList.remove("active"));

// Elementos do cadastro
const cadastroForm = document.getElementById("cadastroForm");
const cadMsg = document.getElementById("cadMsg");

// Elementos do login
const loginForm = document.getElementById("loginForm");
const loginMsg = document.getElementById("loginMsg");

// Salvar usuário no LocalStorage
function salvarUsuario(usuario) {
  localStorage.setItem("sfp_user", JSON.stringify(usuario));
}

// Pegar usuário
function getUsuario() {
  return JSON.parse(localStorage.getItem("sfp_user")) || null;
}

// CADASTRO
cadastroForm.addEventListener("submit", (e) => {
  e.preventDefault();

  const nome = document.getElementById("cadNome").value.trim();
  const email = document.getElementById("cadEmail").value.trim();
  const senha = document.getElementById("cadSenha").value;
  const confirma = document.getElementById("cadConfirma").value;

  if (!nome || !email || !senha || !confirma) {
    cadMsg.textContent = "Preencha todos os campos.";
    cadMsg.className = "msg erro";
    return;
  }

  if (senha !== confirma) {
    cadMsg.textContent = "As senhas não coincidem.";
    cadMsg.className = "msg erro";
    return;
  }

  const usuario = { nome, email, senha };
  salvarUsuario(usuario);

  cadMsg.textContent = "Cadastro realizado com sucesso!";
  cadMsg.className = "msg sucesso";
  cadastroForm.reset();

  setTimeout(() => {
    cadMsg.textContent = "";
    card.classList.remove("active"); // volta ao login
  }, 1500);
});

// LOGIN
loginForm.addEventListener("submit", (e) => {
  e.preventDefault();

  const email = document.getElementById("loginEmail").value.trim();
  const senha = document.getElementById("loginSenha").value;

  const usuario = getUsuario();

  if (!usuario) {
    loginMsg.textContent = "Nenhum usuário cadastrado.";
    loginMsg.className = "msg erro";
    return;
  }

  if (email === usuario.email && senha === usuario.senha) {
    loginMsg.textContent = `Bem-vindo, ${usuario.nome}!`;
    loginMsg.className = "msg sucesso";

    setTimeout(() => {
      loginMsg.textContent = "";
      alert(`Login bem-sucedido!\nBem-vindo, ${usuario.nome}`);
    }, 1000);
  } else {
    loginMsg.textContent = "Email ou senha incorretos.";
    loginMsg.className = "msg erro";
  }
});
