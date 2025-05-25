document.getElementById("todoForm").addEventListener("submit", async function(e) {
  e.preventDefault();

  const itemName = document.getElementById("itemName").value;
  const itemDescription = document.getElementById("itemDescription").value;

  const response = await fetch("http://localhost:5000/submittodoitem", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ itemName, itemDescription })
  });

  const result = await response.json();
  alert(result.message);
});
