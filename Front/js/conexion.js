let queryStrings = new URLSearchParams(window.location.search);
let parametroUrl = Object.fromEntries(queryStrings.entries());

const nombreCategorias = (id) => {
    switch(id){
        case "1":
            document.getElementById("tituloCategoria").innerHTML = "PRODUCTOS DISPONIBLES - BAÑO"
            break;
        case "2":
            document.getElementById("tituloCategoria").innerHTML = "PRODUCTOS DISPONIBLES - CARPINTERIA"
            break;
        case "3":
            document.getElementById("tituloCategoria").innerHTML = "PRODUCTOS DISPONIBLES - COCINA"
            break;
        case "4":
            document.getElementById("tituloCategoria").innerHTML = "PRODUCTOS DISPONIBLES - PINTURA"
            break;
        case "5":
            document.getElementById("tituloCategoria").innerHTML = "PRODUCTOS DISPONIBLES - PISO"
            break;
    }
}

const listProducts = async (id) => {
    
    const response = await fetch("http://127.0.0.1:8000/products/");
    const productos = await response.json();
    
    const response2 = await fetch("http://127.0.0.1:8000/proveedors/");
    const dataProveedor = await response2.json();

    let categoriaActiva = productos.products.filter(function(idCategoria){
        return idCategoria.Id_Categoria_id == id;
    })
    
    let bodyProductos = ``;
    categoriaActiva.forEach((product) => {

        let proveedores = dataProveedor.proveedors.filter(function(element){
            return element.Id_Proveedor == product.Id_Proveedor_id;
        });

        bodyProductos += `
        <div class="productos mt-4 mb-4">
            <img src="${product.Color}" alt="Imagen del producto">
            <h6 class="proveedor mt-1">${proveedores[0].Proveedor}</h6>
            <h4 class="tituloproducto">${product.Producto}</h4>
            <h4 class="descripcionproducto">${pesoCop.format(product.Valor)}</h4>
            <h4 class="descripcionproducto">Color: ${product.Color}</h4>
            <h4 class="descripcionproducto">Material: ${product.Tipo_Material}</h4>
            <a class="contactoproveedor" href="#">CONTACTAR PROVEEDOR</a>
        </div>`
    })
    document.getElementById("productos").innerHTML = bodyProductos;
}

const pesoCop = new Intl.NumberFormat('es-CO', {
    style: 'currency',
    currency: 'COP',
    minimumFractionDigits: 0
})

window.addEventListener("load", function (){
    listProducts(parametroUrl.id);
    nombreCategorias(parametroUrl.id);
})