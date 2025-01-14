// Aplicar a máscara no campo de telefone
document.addEventListener("DOMContentLoaded", function() {
    const telefoneInput = document.querySelector("#id_telefone");
    if (telefoneInput) {
        telefoneInput.addEventListener("input", function() {
            let telefone = telefoneInput.value.replace(/\D/g, "");
            if (telefone.length > 10) {
                telefoneInput.value = telefone.replace(/(\d{2})(\d{5})(\d{4})/, "($1) $2-$3");
            } else {
                telefoneInput.value = telefone.replace(/(\d{2})(\d{4})(\d{4})/, "($1) $2-$3");
            }
        });
    }
});

document.addEventListener("DOMContentLoaded", function() {
    const cnpjInput = document.querySelector("#id_cnpj");  // Altere conforme o nome do campo no formulário
    if (cnpjInput) {
        cnpjInput.addEventListener("input", function() {
            let cnpj = cnpjInput.value.replace(/\D/g, "");  // Remove tudo que não for número
            cnpjInput.value = cnpj
                .replace(/^(\d{2})(\d)/, "$1.$2")
                .replace(/^(\d{2})\.(\d{3})(\d)/, "$1.$2.$3")
                .replace(/\.(\d{3})(\d)/, ".$1/$2")
                .replace(/(\d{4})(\d)/, "$1-$2")
                .substring(0, 18);  // Limita ao tamanho máximo
        });
    }
});
