import streamlit as st
import streamlit.components.v1 as components

# Configuración de la página
st.set_page_config(
    page_title="Dashboard Interactivo - Cuidado del Agua",
    page_icon="💧",
    layout="centered"
)

# Estilos CSS generales (Tonos azul claro y blanco)
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(180deg, #E3F2FD 0%, #FFFFFF 100%);
        }
        .main-header {
            background-color: #FFFFFF;
            padding: 22px;
            border-radius: 20px;
            border: 2px solid #90CAF9;
            text-align: center;
            box-shadow: 0 4px 14px rgba(33, 150, 243, 0.12);
            margin-bottom: 25px;
        }
        .main-title {
            color: #0277BD;
            font-size: 2.2rem;
            font-weight: 800;
            margin: 0;
        }
        .main-subtitle {
            color: #4FC3F7;
            font-size: 1.05rem;
            font-weight: 600;
            margin-top: 6px;
        }
    </style>
""", unsafe_allow_html=True)

# Manejo del estado para cambiar entre el menú y los juegos
if "juego_activo" not in st.session_state:
    st.session_state.juego_activo = "menu"

# --- VISTA: MENÚ PRINCIPAL ---
if st.session_state.juego_activo == "menu":
    st.markdown("""
        <div class="main-header">
            <h1 class="main-title">💧 Centro de Juegos Hídricos</h1>
            <p class="main-subtitle">Elige un minijuego interactivo para aprender sobre el agua y el medio ambiente</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="medium")

    with col1:
        st.markdown("""
            <div style="background: #FFFFFF; border: 2.5px solid #81D4FA; border-radius: 18px; padding: 22px; text-align: center; box-shadow: 0 4px 12px rgba(0,0,0,0.05); height: 100%; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <div style="font-size: 48px; margin-bottom: 8px;">💧</div>
                    <h3 style="color: #01579B; margin: 0 0 10px 0;">AquaPou</h3>
                    <p style="color: #0277BD; font-size: 14px; line-height: 1.4;">
                        Atrapa agua limpia y evita industrias contaminantes (textil, ganadería, petróleo). ¡Incluye datos de impacto global!
                    </p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        if st.button("🎮 Jugar AquaPou", use_container_width=True):
            st.session_state.juego_activo = "pou"
            st.rerun()

    with col2:
        st.markdown("""
            <div style="background: #FFFFFF; border: 2.5px solid #81D4FA; border-radius: 18px; padding: 22px; text-align: center; box-shadow: 0 4px 12px rgba(0,0,0,0.05); height: 100%; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <div style="font-size: 48px; margin-bottom: 8px;">🚰</div>
                    <h3 style="color: #01579B; margin: 0 0 10px 0;">¡Cierra la Llave!</h3>
                    <p style="color: #0277BD; font-size: 14px; line-height: 1.4;">
                        Detén fugas y desperdicios domésticos a contratiempo antes de que se vacíe la reserva de agua. ¡Equivalencias en litros!
                    </p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        if st.button("🎮 Jugar Cierra la Llave", use_container_width=True):
            st.session_state.juego_activo = "llave"
            st.rerun()

# --- VISTA: JUEGO 1 (AQUAPOU) ---
elif st.session_state.juego_activo == "pou":
    if st.button("⬅️ Volver al menú principal"):
        st.session_state.juego_activo = "menu"
        st.rerun()
    
    st.markdown("### 💧 AquaPou: ¡Alimenta la Gota!")
    
    pou_html = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
    <meta charset="UTF-8">
    <style>
        * { box-sizing: border-box; font-family: 'Segoe UI', sans-serif; }
        body { margin: 0; padding: 0; display: flex; justify-content: center; background: transparent; }
        #game-wrapper {
            position: relative; width: 520px; height: 540px; border-radius: 20px; overflow: hidden;
            border: 3px solid #64B5F6; background: linear-gradient(180deg, #E1F5FE 0%, #B3E5FC 65%, #FFFFFF 100%);
            box-shadow: 0 8px 20px rgba(2, 119, 189, 0.15);
        }
        canvas { display: block; width: 100%; height: 100%; cursor: none; }
        #hud { position: absolute; top: 15px; left: 20px; right: 20px; display: flex; justify-content: space-between; pointer-events: none; }
        .badge { background: rgba(255, 255, 255, 0.9); color: #0277BD; padding: 6px 14px; border-radius: 20px; font-weight: bold; font-size: 15px; border: 2px solid #81D4FA; }
        .overlay {
            position: absolute; inset: 0; background: rgba(255, 255, 255, 0.93);
            display: flex; flex-direction: column; justify-content: center; align-items: center; padding: 25px; text-align: center; z-index: 10;
        }
        .hidden { display: none !important; }
        .fact-card {
            background: #E3F2FD; border: 2px solid #42A5F5; border-radius: 14px; padding: 14px; margin: 12px 0 18px 0; color: #0D47A1; text-align: left;
        }
        .fact-card h3 { margin: 0 0 6px 0; color: #D32F2F; font-size: 17px; }
        .fact-card p { margin: 4px 0; font-size: 14px; line-height: 1.4; }
        .btn {
            background: linear-gradient(135deg, #29B6F6, #0288D1); color: white; border: none;
            padding: 10px 24px; font-size: 16px; font-weight: bold; border-radius: 25px; cursor: pointer;
        }
    </style>
    </head>
    <body>
    <div id="game-wrapper">
        <div id="hud">
            <div class="badge">💧 Puntos: <span id="score">0</span></div>
            <div class="badge">🏆 Récord: <span id="highscore">0</span></div>
        </div>
        <canvas id="gameCanvas" width="520" height="540"></canvas>
        <div id="start-screen" class="overlay">
            <div style="font-size: 54px; margin-bottom: 8px;">💧</div>
            <h2 style="color: #01579B; margin: 0 0 8px 0;">¡Alimenta a AquaPou!</h2>
            <p style="color: #0277BD; font-size: 15px; margin-bottom: 18px;">Atrapa agua limpia y evita las industrias contaminantes.</p>
            <button class="btn" onclick="startGame()">¡Empezar a jugar!</button>
        </div>
        <div id="gameover-screen" class="overlay hidden">
            <div style="font-size: 46px;">😵‍💫💦</div>
            <h2 style="color: #C62828; margin: 4px 0;">¡AquaPou se contaminó!</h2>
            <p style="color: #0277BD; font-weight: bold; margin: 0 0 10px 0;">Puntaje: <span id="final-score">0</span> pts</p>
            <div class="fact-card">
                <h3 id="fact-title">⚠️ Impacto</h3>
                <p id="fact-water"></p>
                <p id="fact-country"></p>
            </div>
            <button class="btn" onclick="startGame()">Volver a intentar</button>
        </div>
    </div>
    <script>
    const canvas = document.getElementById("gameCanvas");
    const ctx = canvas.getContext("2d");
    let gameRunning = false, score = 0, highScore = 0, items = [], spawnTimer = 0, speedMultiplier = 1, mouthOpenTimer = 0;
    const pou = { x: canvas.width / 2, y: canvas.height - 60, radius: 36, speed: 8 };
    let keys = { ArrowLeft: false, ArrowRight: false };
    window.addEventListener("keydown", (e) => { if (e.key === "ArrowLeft" || e.key === "ArrowRight") keys[e.key] = true; });
    window.addEventListener("keyup", (e) => { if (e.key === "ArrowLeft" || e.key === "ArrowRight") keys[e.key] = false; });
    canvas.addEventListener("mousemove", (e) => {
        if (!gameRunning) return;
        const rect = canvas.getBoundingClientRect();
        pou.x = Math.max(pou.radius, Math.min(canvas.width - pou.radius, e.clientX - rect.left));
    });
    const GOOD_ITEMS = [{ emoji: "💧", name: "Gota", points: 10 }, { emoji: "🧴", name: "Botella", points: 15 }];
    const BAD_ITEMS = [
        { emoji: "👕", category: "Industria Textil", waterFact: "Consume <b>93 mil millones de m³ de agua al año</b>; unos jeans requieren 7,500 L.", countryFact: "<b>China e India</b> lideran la contaminación por tintes en ríos." },
        { emoji: "🥩", category: "Ganadería Intensiva", waterFact: "Usa casi el <b>30% del agua dulce mundial</b>; 1 kg de res consume ~15,000 L.", countryFact: "<b>Brasil y EE.UU.</b> concentran la mayor huella hídrica ganadera." },
        { emoji: "🛢️", category: "Industria Petrolera", waterFact: "1 litro de petróleo derramado puede contaminar hasta <b>1 millón de litros de agua</b>.", countryFact: "<b>EE.UU. y Rusia</b> lideran extracción; graves daños en Nigeria." },
        { emoji: "🛍️", category: "Plásticos", waterFact: "Más de <b>8 millones de toneladas</b> llegan a océanos cada año.", countryFact: "<b>Filipinas e India</b> encabezan descargas plásticas en ríos." }
    ];
    function startGame() {
        document.getElementById("start-screen").classList.add("hidden");
        document.getElementById("gameover-screen").classList.add("hidden");
        score = 0; items = []; spawnTimer = 0; speedMultiplier = 1; mouthOpenTimer = 0;
        pou.x = canvas.width / 2; document.getElementById("score").innerText = score;
        gameRunning = true; requestAnimationFrame(gameLoop);
    }
    function triggerGameOver(item) {
        gameRunning = false;
        if (score > highScore) { highScore = score; document.getElementById("highscore").innerText = highScore; }
        document.getElementById("final-score").innerText = score;
        document.getElementById("fact-title").innerText = "⚠️ " + item.category;
        document.getElementById("fact-water").innerHTML = "💧 <b>Daño:</b> " + item.waterFact;
        document.getElementById("fact-country").innerHTML = "🌍 <b>Global:</b> " + item.countryFact;
        document.getElementById("gameover-screen").classList.remove("hidden");
    }
    function spawnItem() {
        let isGood = Math.random() < 0.55;
        let template = isGood ? GOOD_ITEMS[Math.floor(Math.random() * GOOD_ITEMS.length)] : BAD_ITEMS[Math.floor(Math.random() * BAD_ITEMS.length)];
        items.push({ x: Math.random() * (canvas.width - 60) + 30, y: -30, radius: 20, speed: (3 + Math.random() * 1.5) * speedMultiplier, isGood, data: template });
    }
    function drawPou() {
        ctx.save(); ctx.translate(pou.x, pou.y);
        ctx.beginPath();
        ctx.moveTo(0, -pou.radius - 10);
        ctx.bezierCurveTo(pou.radius + 10, -4, pou.radius + 6, pou.radius, 0, pou.radius);
        ctx.bezierCurveTo(-pou.radius - 6, pou.radius, -pou.radius - 10, -4, 0, -pou.radius - 10);
        ctx.fillStyle = "#29B6F6"; ctx.fill(); ctx.lineWidth = 2.5; ctx.strokeStyle = "#0288D1"; ctx.stroke();
        // Ojos
        ctx.fillStyle = "white"; ctx.beginPath(); ctx.arc(-10, 3, 7, 0, Math.PI * 2); ctx.arc(10, 3, 7, 0, Math.PI * 2); ctx.fill();
        ctx.fillStyle = "#01579B"; ctx.beginPath(); ctx.arc(-9, 3, 3.5, 0, Math.PI * 2); ctx.arc(9, 3, 3.5, 0, Math.PI * 2); ctx.fill();
        ctx.restore();
    }
    function gameLoop() {
        if (!gameRunning) return;
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        if (keys.ArrowLeft) pou.x = Math.max(pou.radius, pou.x - pou.speed);
        if (keys.ArrowRight) pou.x = Math.min(canvas.width - pou.radius, pou.x + pou.speed);
        spawnTimer++;
        if (spawnTimer >= Math.max(26, Math.floor(50 - score * 0.1))) { spawnItem(); spawnTimer = 0; }
        ctx.font = "32px Arial"; ctx.textAlign = "center"; ctx.textBaseline = "middle";
        for (let i = items.length - 1; i >= 0; i--) {
            let it = items[i]; it.y += it.speed;
            ctx.beginPath(); ctx.arc(it.x, it.y, 20, 0, Math.PI * 2);
            ctx.fillStyle = it.isGood ? "rgba(255,255,255,0.75)" : "rgba(255,235,238,0.85)"; ctx.fill();
            ctx.fillText(it.data.emoji, it.x, it.y + 1);
            if (Math.hypot(it.x - pou.x, it.y - pou.y) < pou.radius + it.radius - 4) {
                if (it.isGood) { score += it.data.points; speedMultiplier = 1 + (score / 220); document.getElementById("score").innerText = score; items.splice(i, 1); continue; }
                else { triggerGameOver(it.data); return; }
            }
            if (it.y > canvas.height + 30) items.splice(i, 1);
        }
        drawPou(); requestAnimationFrame(gameLoop);
    }
    </script>
    </body>
    </html>
    """
    components.html(pou_html, height=560)

# --- VISTA: JUEGO 2 (CIERRA LA LLAVE) ---
elif st.session_state.juego_activo == "llave":
    if st.button("⬅️ Volver al menú principal"):
        st.session_state.juego_activo = "menu"
        st.rerun()

    st.markdown("### 🚰 ¡Cierra la Llave! (Desafío de Ahorro)")

    llave_html = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
    <meta charset="UTF-8">
    <style>
        * { box-sizing: border-box; font-family: 'Segoe UI', sans-serif; user-select: none; }
        body { margin: 0; padding: 0; display: flex; justify-content: center; background: transparent; }
        #container {
            position: relative; width: 520px; background: #FFFFFF; border: 3px solid #64B5F6;
            border-radius: 20px; padding: 18px; box-shadow: 0 8px 20px rgba(2, 119, 189, 0.15);
        }
        #top-bar { display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; }
        .stat-pill { background: #E1F5FE; color: #0277BD; padding: 6px 12px; border-radius: 14px; font-weight: 700; font-size: 14px; border: 1.5px solid #81D4FA; }
        #tank-wrapper { width: 100%; height: 20px; background: #ECEFF1; border-radius: 10px; overflow: hidden; border: 2px solid #90CAF9; margin-bottom: 14px; position: relative; }
        #tank-fill { width: 100%; height: 100%; background: linear-gradient(90deg, #4FC3F7, #0288D1); transition: width 0.2s ease; }
        #tank-label { position: absolute; inset: 0; display: flex; justify-content: center; align-items: center; font-size: 11px; font-weight: 800; color: #01579B; }
        #grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; }
        .pipe-hole {
            height: 105px; background: linear-gradient(180deg, #F0F8FF 0%, #E1F5FE 100%);
            border: 2px solid #B3E5FC; border-radius: 15px; display: flex; flex-direction: column;
            justify-content: center; align-items: center; cursor: pointer; position: relative;
        }
        .pipe-hole.leak { background: #FFF3E0; border-color: #FF9800; }
        .pipe-hole.good { background: #E8F5E9; border-color: #66BB6A; }
        .emoji { font-size: 38px; line-height: 1; }
        .tag { font-size: 10px; font-weight: 700; margin-top: 4px; padding: 2px 6px; border-radius: 6px; }
        .leak .tag { background: #FFE0B2; color: #E65100; }
        .good .tag { background: #C8E6C9; color: #1B5E20; }
        .overlay {
            position: absolute; inset: 0; background: rgba(255, 255, 255, 0.95);
            border-radius: 17px; display: flex; flex-direction: column; justify-content: center; align-items: center; padding: 24px; text-align: center; z-index: 20;
        }
        .hidden { display: none !important; }
        .info-box { background: #E3F2FD; border: 2px solid #42A5F5; border-radius: 12px; padding: 12px; margin: 10px 0 16px 0; color: #0D47A1; font-size: 13.5px; line-height: 1.4; }
        .btn { background: linear-gradient(135deg, #29B6F6, #0288D1); color: white; border: none; padding: 10px 24px; font-size: 15px; font-weight: bold; border-radius: 25px; cursor: pointer; }
    </style>
    </head>
    <body>
    <div id="container">
        <div id="top-bar">
            <div class="stat-pill">⏱️ Tiempo: <span id="time">30</span>s</div>
            <div class="stat-pill">💧 Salvados: <span id="saved">0</span> L</div>
        </div>
        <div id="tank-wrapper">
            <div id="tank-fill"></div>
            <div id="tank-label">Reserva: <span id="tank-pct">100</span>%</div>
        </div>
        <div id="grid"></div>
        <div id="start-overlay" class="overlay">
            <div style="font-size: 50px; margin-bottom: 6px;">🚰💧</div>
            <h2 style="color: #01579B; margin: 0 0 8px 0;">¡Detén las Fugas!</h2>
            <p style="color: #0277BD; font-size: 14px; margin-bottom: 16px;">Haz clic rápido en las fugas antes de que se vacíe el tanque.</p>
            <button class="btn" onclick="startGame()">Comenzar Reto</button>
        </div>
        <div id="end-overlay" class="overlay hidden">
            <div id="end-emoji" style="font-size: 46px;">🎉💧</div>
            <h2 id="end-title" style="color: #01579B; margin: 4px 0;">¡Terminado!</h2>
            <p style="color: #0277BD; font-weight: 700; font-size: 16px; margin: 4px 0;">Salvaste <span id="final-liters">0</span> litros</p>
            <div class="info-box" id="impact-text"></div>
            <button class="btn" onclick="startGame()">Jugar de nuevo</button>
        </div>
    </div>
    <script>
    const grid = document.getElementById("grid");
    let holes = [], timeLeft = 30, savedLiters = 0, tankLevel = 100, gameActive = false, timerInterval, spawnInterval, drainInterval;
    const EVENTS = [
        { type: "leak", emoji: "🚰", label: "Fuga (+20 L)", liters: 20 },
        { type: "leak", emoji: "🚿", label: "Ducha (+50 L)", liters: 50 },
        { type: "leak", emoji: "💦", label: "Manguera (+80 L)", liters: 80 },
        { type: "good", emoji: "🌧️", label: "¡Lluvia!", liters: 0 },
        { type: "good", emoji: "🌱", label: "¡Goteo!", liters: 0 }
    ];
    for (let i = 0; i < 9; i++) {
        const div = document.createElement("div");
        div.className = "pipe-hole";
        div.innerHTML = `<div class="emoji" style="opacity:0.25;">🔵</div>`;
        div.onclick = () => handleHoleClick(i);
        grid.appendChild(div);
        holes.push({ el: div, active: null, timeout: null });
    }
    function updateTankUI() {
        tankLevel = Math.max(0, Math.min(100, tankLevel));
        document.getElementById("tank-fill").style.width = tankLevel + "%";
        document.getElementById("tank-pct").innerText = Math.round(tankLevel);
        if (tankLevel <= 0 && gameActive) endGame(true);
    }
    function clearHole(i) {
        let h = holes[i];
        if (h.timeout) clearTimeout(h.timeout);
        h.active = null; h.el.className = "pipe-hole";
        h.el.innerHTML = `<div class="emoji" style="opacity:0.25;">🔵</div>`;
    }
    function spawnEvent() {
        if (!gameActive) return;
        let free = holes.map((h, i) => h.active === null ? i : -1).filter(i => i !== -1);
        if (free.length === 0) return;
        let idx = free[Math.floor(Math.random() * free.length)];
        let ev = EVENTS[Math.floor(Math.random() * EVENTS.length)];
        let h = holes[idx];
        h.active = ev; h.el.className = "pipe-hole " + ev.type;
        h.el.innerHTML = `<div class="emoji">${ev.emoji}</div><div class="tag">${ev.label}</div>`;
        h.timeout = setTimeout(() => {
            if (h.active && h.active.type === "leak") { tankLevel -= 6; updateTankUI(); }
            clearHole(idx);
        }, 1400);
    }
    function handleHoleClick(i) {
        if (!gameActive) return;
        let h = holes[i]; if (!h.active) return;
        if (h.active.type === "leak") {
            savedLiters += h.active.liters; tankLevel += 3;
            document.getElementById("saved").innerText = savedLiters; updateTankUI();
        } else {
            timeLeft = Math.max(0, timeLeft - 3);
            document.getElementById("time").innerText = timeLeft;
        }
        clearHole(i);
    }
    function startGame() {
        document.getElementById("start-overlay").classList.add("hidden");
        document.getElementById("end-overlay").classList.add("hidden");
        timeLeft = 30; savedLiters = 0; tankLevel = 100; gameActive = true;
        document.getElementById("time").innerText = timeLeft;
        document.getElementById("saved").innerText = savedLiters;
        updateTankUI(); holes.forEach((_, i) => clearHole(i));
        timerInterval = setInterval(() => { timeLeft--; document.getElementById("time").innerText = timeLeft; if (timeLeft <= 0) endGame(false); }, 1000);
        spawnInterval = setInterval(spawnEvent, 600);
        drainInterval = setInterval(() => {
            let leaks = holes.filter(h => h.active && h.active.type === "leak").length;
            if (leaks > 0) { tankLevel -= leaks * 1.3; updateTankUI(); }
        }, 350);
    }
    function endGame(empty) {
        gameActive = false; clearInterval(timerInterval); clearInterval(spawnInterval); clearInterval(drainInterval);
        holes.forEach((_, i) => clearHole(i));
        document.getElementById("final-liters").innerText = savedLiters;
        let people = Math.floor(savedLiters / 100), days = Math.floor(savedLiters / 2);
        document.getElementById("end-emoji").innerText = empty ? "🏜️⚠️" : "🎉💧";
        document.getElementById("end-title").innerText = empty ? "¡Se agotó el tanque!" : "¡Buen trabajo!";
        document.getElementById("impact-text").innerHTML = `🌍 Con <b>${savedLiters} litros</b> salvados cubres el consumo básico de <b>${people} persona(s)</b> por un día o bebida por <b>${days} días</b>.`;
        document.getElementById("end-overlay").classList.remove("hidden");
    }
    </script>
    </body>
    </html>
    """
    components.html(llave_html, height=520)
