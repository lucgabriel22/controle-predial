document.addEventListener('DOMContentLoaded', function() {
    ordenarPorNumerodaCasa();
});

function ordenarPorNumerodaCasa() {
    var tbody = document.getElementById('tabela-corpo');
    var linhas = Array.from(tbody.rows).slice(0); // Converte a coleção de linhas em um array

    linhas.sort(function (a, b) {
        var casaA = parseInt(a.cells[1].textContent.trim());
        var casaB = parseInt(b.cells[1].textContent.trim());
        console.log('Casa A:', casaA); // Adiciona console log para Casa A
        console.log('Casa B:', casaB); // Adiciona console log para Casa B
        return casaA - casaB;
    });

    linhas.forEach(function (linha) {
        tbody.appendChild(linha);
    });
}