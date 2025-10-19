const tbody = document.querySelector("tbody");
const descitem = document.querySelector("#desc");
const amount = document.querySelector("#Amount");
const type = document.querySelector("#type");
const btn = document.querySelector("#btnNew");

const incomes = document.querySelector(".incomes");
const expenses = document.querySelector(".expenses");
const total = document.querySelector(".total");

let itens = getItensBD();

btn.addEventListener("click", () => {
  if (descitem.value === "" || amount.value === "" || type.value === "") {
    return alert("Por favor, preencha todos os campos!");
  }

  itens.push({
    desc: descitem.value,
    amount: parseFloat(amount.value).toFixed(2),
    type: type.value,
  });

  setItensBD();
  loadItens();

  descitem.value = "";
  amount.value = "";
});

function deleteItem(index) {
  itens.splice(index, 1);
  setItensBD();
  loadItens();
}

function insertItem(item, index) {
  const tr = document.createElement("tr");
  tr.innerHTML = `
    <td>${item.desc}</td>
    <td>R$ ${item.amount}</td>
    <td class="columnType">
      ${
        item.type === "Entrada"
          ? '<i class="bx bxs-chevron-up-circle" style="color:#00c9a7;"></i>'
          : '<i class="bx bxs-chevron-down-circle" style="color:#d83121;"></i>'
      }
    </td>
    <td class="columnAction">
      <button onclick="deleteItem(${index})"><i class='bx bxs-trash'></i></button>
    </td>
  `;
  tbody.appendChild(tr);
}

function loadItens() {
  itens = getItensBD();
  tbody.innerHTML = "";
  itens.forEach((item, index) => insertItem(item, index));
  updateTotals();
}

function updateTotals() {
  const totalIncomes = itens
    .filter(i => i.type === "Entrada")
    .reduce((acc, cur) => acc + Number(cur.amount), 0)
    .toFixed(2);

  const totalExpenses = itens
    .filter(i => i.type === "Saída")
    .reduce((acc, cur) => acc + Number(cur.amount), 0)
    .toFixed(2);

  const totalAmount = (totalIncomes - totalExpenses).toFixed(2);

  incomes.textContent = totalIncomes;
  expenses.textContent = totalExpenses;
  total.textContent = totalAmount;
}

function getItensBD() {
  return JSON.parse(localStorage.getItem("itens")) ?? [];
}

function setItensBD() {
  localStorage.setItem("itens", JSON.stringify(itens));
}

loadItens();
