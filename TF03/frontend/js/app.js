const API = "/api/posts";

// Listar posts
async function carregarPosts() {
  const res = await fetch(API);
  const posts = await res.json();

  const container = document.getElementById("posts");
  if (!container) return;

  container.innerHTML = posts.map(p => `
    <div>
      <h3>${p.title}</h3>
      <p>${p.content}</p>
    </div>
  `).join("");
}

// Criar post
async function criarPost() {
  const title = document.getElementById("title").value;
  const content = document.getElementById("content").value;

  if (!title.trim() || !content.trim()) {
    alert("Título e conteúdo são obrigatórios.");
    return;
  }

  const res = await fetch(API, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ title, content })
  });

  if (!res.ok) {
    const err = await res.text();
    alert(`Erro ao criar post: ${err}`);
    return;
  }

  alert("Post criado!");
  document.getElementById("title").value = "";
  document.getElementById("content").value = "";
  carregarPosts();
}

carregarPosts();