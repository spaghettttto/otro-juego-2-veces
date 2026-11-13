import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="¡Cierra la Llave! - Ahorro de Agua",
    page_icon="🚰",
    layout="centered"
)

# Estilos CSS personalizados (Azul claro y blanco)
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(180deg, #E3F2FD 0%, #FFFFFF 100%);
        }
        .header-box {
            background-color: #FFFFFF;
            padding: 18px;
            border-radius: 18px;
            border: 2px solid #90CAF9;
            text-align: center;
            box-shadow: 0 4px 12px rgba(33, 150, 243, 0.12);
            margin-bottom: 12px;
        }
        .header-title {
            color: #0277BD;
            font-size: 2rem;
            font-weight: 800;
            margin: 0;
        }
        .header-subtitle {
            color: #4FC3F7;
            font-size: 1rem;
            font-weight: 600;
            margin-top: 4px;
        }
        .legend-box {
            background-color: #F0F8FF;
            border-left: 5px solid #29B6F6;
            padding: 10px 16px;
            border-radius: 10px;
            color: #01579B;
            font-size: 0.92rem;
            margin-bottom: 12px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="header-box">
        <h1 class="header-title">🚰 ¡Cierra la Llave!</h1>
        <p class="header-subtitle">Detén las fugas y el desperdicio antes de que se vacíe la reserva</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="legend-box">
        <b>Instrucciones:</b> Haz clic rápido sobre las fugas para cerrarlas.<br>
        ✅ <b>Cierra (+Litros salvados):</b> Llave abierta (🚰), Ducha larga (🚿), Manguera (💦).<br>
        ⚠️ <b>¡No toques! (-3 seg):</b> Agua de lluvia (🌧️) y Riego eficiente (🌱).
    </div>
""", unsafe_allow_html=True)

game_html = """
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<style>
    * {
        box-sizing: border-box;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        user-select: none;
    }
    body {
        margin: 0;
        padding: 0;
        display: flex;
        justify-content: center;
        background: transparent;
    }
    #container {
        position: relative;
        width: 520px;
        background: #FFFFFF;
        border: 3px solid #64B5F6;
        border-radius: 20px;
        padding: 20px;
        box-shadow: 0 8px 20px rgba(2, 119, 189, 0.15);
    }
    #top-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 12px;
    }
    .stat-pill {
        background: #E1F5FE;
        color: #0277BD;
        padding: 8px 14px;
        border-radius: 15px;
        font-weight: 700;
        font-size: 15px;
        border: 1.5px solid #81D4FA;
    }
    /* Barra de nivel del tanque */
    #tank-wrapper {
        width: 100%;
        height: 22px;
        background: #ECEFF1;
        border-radius: 12px;
        overflow: hidden;
        border: 2px solid #90CAF9;
        margin-bottom: 18px;
        position: relative;
    }
    #tank-fill {
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, #4FC3F7, #0288D1);
        transition: width 0.2s ease, background 0.3s ease;
    }
    #tank-label {
        position: absolute;
        inset: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 12px;
        font-weight: 800;
        color: #01579B;
    }
    /* Cuadrícula 3x3 */
    #grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 14px;
    }
    .pipe-hole {
        height: 115px;
        background: linear-gradient(180deg, #F0F8FF 0%, #E1F5FE 100%);
        border: 2.5px solid #B3E5FC;
        border-radius: 18px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        cursor: pointer;
        transition: transform 0.1s ease, background 0.15s ease;
        position: relative;
    }
    .pipe-hole:active {
        transform: scale(0.94);
    }
    .pipe-hole.leak {
        background: #FFF3E0;
        border-color: #FF9800;
        animation: pulse 0.6s infinite alternate;
    }
    .pipe-hole.good {
        background: #E8F5E9;
        border-color: #66BB6A;
    }
    .emoji {
        font-size: 42px;
        line-height: 1;
    }
    .tag {
        font-size: 11px;
        font-weight: 700;
        margin-top: 6px;
        padding: 2px 8px;
        border-radius: 8px;
    }
    .leak .tag {
        background: #FFE0B2;
        color: #E65100;
    }
    .good .tag {
        background: #C8E6C9;
        color: #1B5E20;
    }
    @keyframes pulse {
        from { transform: scale(1); }
        to { transform: scale(1.03); }
    }
    /* Pantallas superpuestas */
    .overlay {
        position: absolute;
        inset: 0;
        background: rgba(255, 255, 255, 0.95);
        border-radius: 17px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        padding: 28px;
        text-align: center;
        z-index: 20;
    }
    .hidden { display: none !important; }
    .info-box {
        background: #E3F2FD;
        border: 2px solid #42A5F5;
        border-radius: 14px;
        padding: 16px;
        margin: 14px 0 20px 0;
        color: #0D47A1;
        font-size: 14.5px;
        line-height: 1.5;
    }
    .btn {
        background: linear-gradient(135deg, #29B6F6, #0288D1);
        color: white;
        border: none;
        padding: 12px 28px;
        font-size: 16px;
        font-weight: bold;
        border-radius: 25px;
        cursor: pointer;
        box-shadow: 0 4px 12px rgba(2, 136, 209, 0.3);
    }
    .btn:hover { transform: scale(1.04); }
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
        <div id="tank-label">Reserva de Agua: <span id="tank-pct">100</span>%</div>
    </div>

    <div id="grid"></div>

    <!-- Pantalla inicial -->
    <div id="start-overlay" class="overlay">
        <div style="font-size: 56px; margin-bottom: 8px;">🚰💧</div>
        <h2 style="color: #01579B; margin: 0 0 10px 0;">¡Detén las Fugas!</h2>
        <p style="color: #0277BD; font-size: 15px; margin-bottom: 20px;">
            Una llave que gotea puede perder hasta <b>30 litros al día</b>. Haz clic rápido en las fugas antes de que se agote el tanque.
        </p>
        <button class="btn" onclick="startGame()">Comenzar Reto</button>
    </div>

    <!-- Pantalla final -->
    <div id="end-overlay" class="overlay hidden">
        <div id="end-emoji" style="font-size: 52px;">🎉💧</div>
        <h2 id="end-title" style="color: #01579B; margin: 6px 0;">¡Tiempo terminado!</h2>
        <p style="color: #0277BD; font-weight: 700; font-size: 17px; margin: 4px 0;">
            Lograste salvar <span id="final-liters">0</span> litros de agua
        </p>
        <div class="info-box" id="impact-text"></div>
        <button class="btn" onclick="startGame()">Jugar de nuevo</button>
    </div>
</div>

<script>
const grid = document.getElementById("grid");
const TOTAL_HOLES = 9;
let holes = [];
let timeLeft = 30;
let savedLiters = 0;
let tankLevel = 100;
let gameActive = false;
let timerInterval = null;
let spawnInterval = null;
let drainInterval = null;

const EVENTS = [
    { type: "leak", emoji: "🚰", label: "Fuga (+20 L)", liters: 20 },
    { type: "leak", emoji: "🚿", label: "Ducha (+50 L)", liters: 50 },
    { type: "leak", emoji: "💦", label: "Manguera (+80 L)", liters: 80 },
    { type: "good", emoji: "🌧️", label: "¡Lluvia! No tocar", liters: 0 },
    { type: "good", emoji: "🌱", label: "¡Goteo! No tocar", liters: 0 }
];

// Crear las 9 celdas
for (let i = 0; i < TOTAL_HOLES; i++) {
    const div = document.createElement("div");
    div.className = "pipe-hole";
    div.innerHTML = `<div class="emoji" style="opacity:0.25;">🔵</div>`;
    div.onclick = () => handleHoleClick(i);
    grid.appendChild(div);
    holes.push({ el: div, active: null, timeout: null });
}

function updateTankUI() {
    tankLevel = Math.max(0, Math.min(100, tankLevel));
    const fill = document.getElementById("tank-fill");
    fill.style.width = tankLevel + "%";
    document.getElementById("tank-pct").innerText = Math.round(tankLevel);

    if (tankLevel < 30) {
        fill.style.background = "linear-gradient(90deg, #EF5350, #C62828)";
    } else if (tankLevel < 60) {
        fill.style.background = "linear-gradient(90deg, #FFA726, #EF6C00)";
    } else {
        fill.style.background = "linear-gradient(90deg, #4FC3F7, #0288D1)";
    }

    if (tankLevel <= 0 && gameActive) {
        endGame(true);
    }
}

function clearHole(index) {
    const h = holes[index];
    if (h.timeout) clearTimeout(h.timeout);
    h.active = null;
    h.el.className = "pipe-hole";
    h.el.innerHTML = `<div class="emoji" style="opacity:0.25;">🔵</div>`;
}

function spawnEvent() {
    if (!gameActive) return;
    const freeIndices = holes.map((h, idx) => h.active === null ? idx : -1).filter(idx => idx !== -1);
    if (freeIndices.length === 0) return;

    const idx = freeIndices[Math.floor(Math.random() * freeIndices.length)];
    const ev = EVENTS[Math.floor(Math.random() * EVENTS.length)];
    const h = holes[idx];

    h.active = ev;
    h.el.className = "pipe-hole " + ev.type;
    h.el.innerHTML = `<div class="emoji">${ev.emoji}</div><div class="tag">${ev.label}</div>`;

    h.timeout = setTimeout(() => {
        if (h.active && h.active.type === "leak") {
            tankLevel -= 7; // Penalización si se deja abierta la fuga
            updateTankUI();
        }
        clearHole(idx);
    }, 1500);
}

function handleHoleClick(index) {
    if (!gameActive) return;
    const h = holes[index];
    if (!h.active) return;

    if (h.active.type === "leak") {
        savedLiters += h.active.liters;
        tankLevel += 3;
        document.getElementById("saved").innerText = savedLiters;
        updateTankUI();
    } else {
        // Penalización por cerrar captación de lluvia o riego eficiente
        timeLeft = Math.max(0, timeLeft - 3);
        document.getElementById("time").innerText = timeLeft;
    }
    clearHole(index);
}

function startGame() {
    document.getElementById("start-overlay").classList.add("hidden");
    document.getElementById("end-overlay").classList.add("hidden");

    timeLeft = 30;
    savedLiters = 0;
    tankLevel = 100;
    gameActive = true;

    document.getElementById("time").innerText = timeLeft;
    document.getElementById("saved").innerText = savedLiters;
    updateTankUI();

    holes.forEach((_, idx) => clearHole(idx));

    timerInterval = setInterval(() => {
        timeLeft--;
        document.getElementById("time").innerText = timeLeft;
        if (timeLeft <= 0) {
            endGame(false);
        }
    }, 1000);

    spawnInterval = setInterval(spawnEvent, 650);

    drainInterval = setInterval(() => {
        const activeLeaks = holes.filter(h => h.active && h.active.type === "leak").length;
        if (activeLeaks > 0) {
            tankLevel -= activeLeaks * 1.5;
            updateTankUI();
        }
    }, 400);
}

function endGame(emptyTank) {
    gameActive = false;
    clearInterval(timerInterval);
    clearInterval(spawnInterval);
    clearInterval(drainInterval);
    holes.forEach((_, idx) => clearHole(idx));

    document.getElementById("final-liters").innerText = savedLiters;

    const peopleDays = Math.floor(savedLiters / 100);
    const drinkingDays = Math.floor(savedLiters / 2);

    if (emptyTank) {
        document.getElementById("end-emoji").innerText = "🏜️⚠️";
        document.getElementById("end-title").innerText = "¡Se agotó el tanque!";
    } else {
        document.getElementById("end-emoji").innerText = "🎉💧";
        document.getElementById("end-title").innerText = "¡Buen trabajo!";
    }

    document.getElementById("impact-text").innerHTML = `
        🌍 <b>¿Qué significa tu ahorro?</b><br>
        Con <b>${savedLiters} litros</b> de agua salvados podrías cubrir el consumo básico diario de <b>${peopleDays} persona(s)</b> (según la OMS son ~100 L/día) o darle agua para beber a alguien durante <b>${drinkingDays} días</b>.
    `;

    document.getElementById("end-overlay").classList.remove("hidden");
}
</script>
</body>
</html>
"""

components.html(game_html, height=540)
