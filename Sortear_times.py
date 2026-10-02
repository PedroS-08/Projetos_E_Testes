import streamlit as st
import streamlit.components.v1 as components
import random


JOGADORES = [
    {"nome": "Alan", "nota": 6.5, "posicao": "MEI"},
    {"nome": "Artin", "nota": 5.2, "posicao": "ATA"},
    {"nome": "Augusto", "nota": 2.5, "posicao": "DEF"},
    {"nome": "Bernardo", "nota": 6.5, "posicao": "ATA"},
    {"nome": "Caio", "nota": 3.0, "posicao": "DEF"},
    {"nome": "Chu", "nota": 8.0, "posicao": "ATA"},
    {"nome": "Cipriani", "nota": 9.5, "posicao": "MEI"},
    {"nome": "Cleber", "nota": 7.5, "posicao": "DEF"},
    {"nome": "Conrado", "nota": 5.5, "posicao": "ATA"},
    {"nome": "Davi", "nota": 6.0, "posicao": "ATA"},
    {"nome": "Davi Mogli", "nota": 8.0, "posicao": "ATA"},
    {"nome": "Dinali", "nota": 3.0, "posicao": "ATA"},
    {"nome": "Didi", "nota": 5.5, "posicao": "DEF"},
    {"nome": "Diego", "nota": 6.2, "posicao": "DEF"},
    {"nome": "Gabriel", "nota": 7.5, "posicao": "ATA"},
    {"nome": "Guilherme", "nota": 5.0, "posicao": "MEI"},
    {"nome": "Gui", "nota": 6.5, "posicao": "DEF"},
    {"nome": "Gusta", "nota": 8.0, "posicao": "MEI"},
    {"nome": "Hick D", "nota": 4.2, "posicao": "DEF"},
    {"nome": "João V.", "nota": 6.2, "posicao": "MEI"},
    {"nome": "João-limar", "nota": 5.5, "posicao": "ATA"},
    {"nome": "Julis", "nota": 7.5, "posicao": "MEI"},
    {"nome": "Kaio Giarola", "nota": 6.0, "posicao": "ATA"},
    {"nome": "Lacerda", "nota": 5.0, "posicao": "ATA"},
    {"nome": "Leo", "nota": 4.0, "posicao": "DEF"},
    {"nome": "Luiz", "nota": 7.0, "posicao": "ATA"},
    {"nome": "Maladeza", "nota": 6.0, "posicao": "ATA"},
    {"nome": "Marcos", "nota": 9.0, "posicao": "MEI"},
    {"nome": "Matheus", "nota": 7.0, "posicao": "ATA"},
    {"nome": "Nicolas", "nota": 9.2, "posicao": "ATA"},
    {"nome": "Otávio", "nota": 7.5, "posicao": "DEF"},
    {"nome": "Pedrão", "nota": 5.2, "posicao": "DEF"},
    {"nome": "Pedro", "nota": 9.0, "posicao": "MEI"},
    {"nome": "Pedrin", "nota": 6.5, "posicao": "DEF"},
    {"nome": "Prejuízo", "nota": 6.0, "posicao": "ATA"},
    {"nome": "Renan", "nota": 4.5, "posicao": "MEI"},
    {"nome": "Rios", "nota": 7.5, "posicao": "ATA"},
    {"nome": "Ryan", "nota": 6.5, "posicao": "DEF"},
    {"nome": "Samuka", "nota": 7.2, "posicao": "MEI"},
    {"nome": "Schettini", "nota": 5.5, "posicao": "MEI"},
    {"nome": "Surdin", "nota": 9.0, "posicao": "MEI"},
    {"nome": "Thiago", "nota": 7.5, "posicao": "ATA"},
    {"nome": "Thiago Bisnaga", "nota": 6.5, "posicao": "MEI"},
    {"nome": "Trufa", "nota": 2.5, "posicao": "DEF"},
    {"nome": "Tulin", "nota": 7.5, "posicao": "DEF"},
    {"nome": "Wilson", "nota": 7.0, "posicao": "DEF"},
]

REGRAS_GOLEIRO = {
    "Pedrão": {"linha": 5.0, "gol": 7.0},
    "Tulin":  {"linha": 5.0, "gol": 8.5},
    "Otávio": {"linha": 5.0, "gol": 7.5},
    "Trufa":  {"linha": 3.0, "gol": 6.5},
    "Gusta":  {"linha": 7.5, "gol": 8.0},
    "Ryan":  {"linha": 5.0, "gol": 6.5},
    "Hick D":  {"linha": 4.2, "gol": 6.5},
}

NOMES_TIMES = {
    2: ["Time Preto", "Time Branco"],
    3: ["Time Preto", "Time Branco", "Time Azul"],
    4: ["Time Preto", "Time Branco", "Time Azul", "Time Amarelo"],
}

EMOJI_TIMES = {
    "Time Preto": "⚫",
    "Time Branco": "⚪",
    "Time Azul": "🔵",
    "Time Amarelo": "🟡",
}

st.set_page_config(page_title="Sorteador de Times",
                   page_icon="⚽", layout="centered")

st.title("⚽ Sorteador de Times Fut")
st.write("Marque quem vai jogar e escolha quantos times dividir.")


st.header("Quem vai jogar hoje:")

c1, c2, c3 = st.columns(3)
with c1:
    marcar_todos = st.button("✅ Marcar todos")
with c2:
    desmarcar_todos = st.button("❌ Desmarcar todos")
with c3:
    st.write(f"Cadastrados: **{len(JOGADORES)}**")

for j in JOGADORES:
    chave = f"presente_{j['nome']}"
    if chave not in st.session_state:
        st.session_state[chave] = True
    if marcar_todos:
        st.session_state[chave] = True
    if desmarcar_todos:
        st.session_state[chave] = False

cols = st.columns(3)
for i, j in enumerate(JOGADORES):
    chave = f"presente_{j['nome']}"
    with cols[i % 3]:
        st.checkbox(f"{j['nome']}", key=chave)

selecionados_base = [
    j for j in JOGADORES if st.session_state[f"presente_{j['nome']}"]]
qtd_selecionados = len(selecionados_base)

st.markdown(f"**Jogadores selecionados: {qtd_selecionados}**")


especiais_selecionados = [
    j for j in selecionados_base if j["nome"] in REGRAS_GOLEIRO]

if especiais_selecionados:
    st.header("Gol ou linha?")
    st.caption("Alguns jogadores selecionados podem ser goleiros fixos.")
    for j in especiais_selecionados:
        chave_pos = f"posicao_{j['nome']}"
        if chave_pos not in st.session_state:
            st.session_state[chave_pos] = "Linha"
        st.radio(
            f"{j['nome']} vai jogar no:",
            options=["Linha", "Gol"],
            key=chave_pos,
            horizontal=True,
        )


selecionados = []
for j in selecionados_base:
    nome = j["nome"]
    if nome in REGRAS_GOLEIRO:
        posicao = st.session_state.get(f"posicao_{nome}", "Linha")
        eh_gol = posicao == "Gol"
        nota_efetiva = REGRAS_GOLEIRO[nome]["gol"] if eh_gol else REGRAS_GOLEIRO[nome]["linha"]
    else:
        eh_gol = False
        nota_efetiva = j["nota"]
    selecionados.append({
        "nome": nome,
        "nota": nota_efetiva,
        "gol": eh_gol,
        "posicao": j["posicao"]
    })


st.header("Quantidade de times")

opcoes_validas = [n for n in (
    2, 3, 4) if qtd_selecionados > 0 and qtd_selecionados % n == 0]

if not opcoes_validas:
    st.error(
        f"Não é possível dividir {qtd_selecionados} jogadores igualmente em 2, 3 ou 4 times. "
        "Ajuste a quantidade de jogadores selecionados."
    )
    num_times = None
else:
    num_times = st.radio(
        "Times",
        options=opcoes_validas,
        format_func=lambda n: f"{n} times ({qtd_selecionados // n} jogadores cada)",
        horizontal=True,
    )


def montar_times(jogadores, num_times):
    time_size = len(jogadores) // num_times

    times = [[] for _ in range(num_times)]
    somas = [0.0] * num_times

    limites = {
        "DEF": 2,
        "MEI": 1,
        "ATA": 2
    }

    goleiros = [j for j in jogadores if j.get("gol")]
    linha = [j for j in jogadores if not j.get("gol")]

    random.shuffle(goleiros)
    ordem_times = list(range(num_times))
    random.shuffle(ordem_times)

    aviso_goleiros_duplicados = False

    idx_time = 0

    for g in goleiros:
        candidatos = [
            i for i in range(num_times)
            if len(times[i]) < time_size
        ]

        candidatos_sem_goleiro = [
            i for i in candidatos
            if not any(p.get("gol") for p in times[i])
        ]

        if candidatos_sem_goleiro:
            candidatos = candidatos_sem_goleiro

        time_escolhido = min(
            candidatos,
            key=lambda i: somas[i]
        )

        if any(p.get("gol") for p in times[time_escolhido]):
            aviso_goleiros_duplicados = True

        times[time_escolhido].append(g)
        somas[time_escolhido] += g["nota"]

    random.shuffle(linha)
    linha.sort(key=lambda j: j["nota"], reverse=True)

    for jogador in linha:
        posicao = jogador.get("posicao", "ATA")

        candidatos = []

        for i in range(num_times):
            if len(times[i]) >= time_size:
                continue

            quantidade_posicao = sum(
                1 for p in times[i]
                if p.get("posicao") == posicao
            )

            if quantidade_posicao < limites[posicao]:
                candidatos.append(i)

        if not candidatos:
            candidatos = [
                i for i in range(num_times)
                if len(times[i]) < time_size
            ]

        time_escolhido = min(
            candidatos,
            key=lambda i: somas[i]
        )

        times[time_escolhido].append(jogador)
        somas[time_escolhido] += jogador["nota"]

    return times, aviso_goleiros_duplicados


def montar_texto_copia(times, nomes_times):
    blocos = []
    for i, time in enumerate(times):
        nome_time = nomes_times[i]
        emoji = EMOJI_TIMES.get(nome_time, "")
        linhas = [f"Time {nome_time.replace('Time ', '')} {emoji}:"]
        for j in sorted(time, key=lambda x: x["nota"], reverse=True):
            linhas.append(f"- {j['nome']}")
        blocos.append("\n".join(linhas))
    return "\n\n".join(blocos)


def botao_copiar(texto, key):
    texto_escapado = (
        texto.replace("\\", "\\\\")
        .replace("`", "\\`")
        .replace("${", "\\${")
    )
    html_code = f"""
    <div style="font-family: 'Source Sans Pro', sans-serif;">
        <button id="btn_{key}" style="
            padding:8px 18px;
            border-radius:8px;
            border:1px solid #ccc;
            background-color:#FF4B4B;
            color:white;
            font-size:14px;
            font-weight:600;
            cursor:pointer;
        ">📋 Copiar</button>
        <span id="msg_{key}" style="margin-left:10px;color:#2ECC71;font-size:14px;font-weight:600;"></span>
    </div>
    <textarea id="texto_{key}" style="position:absolute; left:-9999px; top:-9999px;">{texto}</textarea>
    <script>
    const btn_{key} = document.getElementById("btn_{key}");
    btn_{key}.addEventListener("click", function() {{
        const texto = `{texto_escapado}`;
        function marcarCopiado() {{
            document.getElementById("msg_{key}").innerText = "Copiado!";
            setTimeout(function() {{
                document.getElementById("msg_{key}").innerText = "";
            }}, 2000);
        }}
        if (navigator.clipboard && window.isSecureContext) {{
            navigator.clipboard.writeText(texto).then(marcarCopiado).catch(function() {{
                const ta = document.getElementById("texto_{key}");
                ta.focus();
                ta.select();
                document.execCommand("copy");
                marcarCopiado();
            }});
        }} else {{
            const ta = document.getElementById("texto_{key}");
            ta.focus();
            ta.select();
            document.execCommand("copy");
            marcarCopiado();
        }}
    }});
    </script>
    """
    components.html(html_code, height=50)


st.header("Sorteio")

sortear = st.button("🔀 Sortear times", disabled=(num_times is None))

if sortear and num_times:
    times, aviso = montar_times(selecionados, num_times)
    st.session_state["ultimo_sorteio"] = times
    st.session_state["aviso_goleiros"] = aviso
    st.session_state["ultimo_num_times"] = num_times

if "ultimo_sorteio" in st.session_state and num_times and st.session_state.get("ultimo_num_times") == num_times:
    times = st.session_state["ultimo_sorteio"]
    nomes_times = NOMES_TIMES[num_times]

    if st.session_state.get("aviso_goleiros"):
        st.warning(
            "Há mais goleiros do que times, então tem time com mais de um"
        )

    cols = st.columns(len(times))
    for i, time in enumerate(times):
        soma = sum(j["nota"] for j in time)
        media = soma / len(time) if time else 0
        with cols[i]:
            st.subheader(nomes_times[i])
            for j in sorted(time, key=lambda x: x["nota"], reverse=True):
                marcador = " GOL" if j.get("gol") else ""
                st.write(f"{j['nome']} — {j.get('posicao', '')}{marcador}")
            st.markdown(f"**Soma:** {soma:.1f}  \n**Média:** {media:.2f}")

    somas = [sum(j["nota"] for j in t) for t in times]
    diferenca = max(somas) - min(somas)
    st.info(
        f"Diferença entre o time mais forte e o mais fraco: **{diferenca:.1f} pontos**")

    st.markdown("---")
    texto_copia = montar_texto_copia(times, nomes_times)
    botao_copiar(texto_copia, key="copiar_times")

    if st.button("🔁 Sortear novamente"):
        times, aviso = montar_times(selecionados, num_times)
        st.session_state["ultimo_sorteio"] = times
        st.session_state["aviso_goleiros"] = aviso
        st.rerun()
