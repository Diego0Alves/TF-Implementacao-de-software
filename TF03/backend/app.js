const express = require("express");
const mysql = require("mysql2");
const app = express();

app.use(express.json());

// Conexão com banco
const db = mysql.createConnection({
  host: process.env.DB_HOST,
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  database: process.env.DB_NAME,
});

db.connect(err => {
  if (err) {
    console.error("Erro DB:", err);
    return;
  }
  console.log("Conectado ao MySQL");
});

// Healthcheck
app.get("/health", (req, res) => res.send("OK"));

// GET posts
app.get("/posts", (req, res) => {
  db.query("SELECT * FROM posts", (err, results) => {
    if (err) return res.status(500).json(err);
    res.json(results);
  });
});

// GET post por id
app.get("/posts/:id", (req, res) => {
  db.query("SELECT * FROM posts WHERE id = ?", [req.params.id], (err, results) => {
    if (err) return res.status(500).json(err);
    res.json(results[0]);
  });
});

// POST novo post
app.post("/posts", (req, res) => {
  const { title, content } = req.body;
  db.query(
    "INSERT INTO posts (title, content) VALUES (?, ?)",
    [title, content],
    (err, result) => {
      if (err) return res.status(500).json(err);
      res.json({ id: result.insertId });
    }
  );
});

app.listen(5000, () => console.log("Backend rodando na porta 5000"));