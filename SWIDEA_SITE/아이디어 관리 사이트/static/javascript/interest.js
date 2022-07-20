const plus = (id) => {
  let interest = document.getElementById(id).innerText;
  interest++;
  document.getElementById(id).innerText = interest;
  const { data } = axios.post("/", { id, interest });
};

const minus = (id) => {
  let interest = document.getElementById(id).innerText;
  interest--;
  document.getElementById(id).innerText = interest;
  const { data } = axios.post("/", { id, interest });
};
