const listarProveedores = async () => {

    const resProveedors = await fetch('https://remodelapp.pythonanywhere.com/proveedors/');
    const dataProveedors = await resProveedors.json();

    let proveedores = `<option value="">SELECCIONE EL PROVEEDOR</option>`
    dataProveedors.proveedors.forEach(proveedor => {
        proveedores += `
        <option value="${proveedor.Id_Proveedor}">${proveedor.Proveedor}</option>`
    });

    document.getElementById("proveedor").innerHTML = proveedores;
}

const crearProducto = async () => {

    let nombre = document.getElementById("name").value;
    let categoria = document.getElementById("categoria").value;
    let proveedor = document.getElementById("proveedor").value;
    let valor = document.getElementById("valor").value;
    let color = document.getElementById("color").value;
    let tipo = document.getElementById("tipo").value;

    const response = await fetch('https://remodelapp.pythonanywhere.com/products/', {
            method: 'POST',
            headers: {
                'Content-Type':'application/json'
            },
            mode: 'cors',
            body: JSON.stringify([{
                "Producto": nombre,
                "Id_Categoria_id": categoria,
                "Id_Proveedor_id": proveedor,
                "Valor": valor,
                "Color": color,
                "Tipo_Material": tipo
            }]),
        })

    let data = await response;
    console.log(data)
    
}

window.addEventListener("load", function(){
    listarProveedores();
})

document.getElementById("enviar").addEventListener("click", function(){
    crearProducto();
})