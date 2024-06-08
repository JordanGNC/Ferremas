
const cboBoleta = document.getElementById('infoBoleta');
const listaBoleta = fetch("http://localhost:5002/api/boleta/", {
    headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
    },
    mode: 'cors'
});

const cboCliente = document.getElementById('infoCliente');
const listaClientes = fetch("http://localhost:5002/api/cliente", {
    headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
    },
    mode: 'cors'
});
const cboProducto = document.getElementById('infoProducto');
const listaProductos = fetch("http://localhost:5002/api/Producto", {
    headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
    },
    mode: 'cors'
});

const cboSubProducto = document.getElementById('infoSubProducto');
const listaSubProductos = fetch("http://localhost:5002/api/Producto", {
    headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
    },
    mode: 'cors'
});

const txtPrecio = document.getElementById('infoPrecio');
const listaPrecio = fetch("http://localhost:5002/api/Producto", {
    headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
    },
    mode: 'cors'
});
const txtCantidad = document.getElementById('infoCantidad');

const txtTotal = document.getElementById('infoTotal');
const listaTotal = fetch("http://localhost:5002/api/boleta/", {
    headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
    },
    mode: 'cors'
});
const txtMarca = document.getElementById('infoMarca');
const txtTipo = document.getElementById('infoTipo');

// listado y funcion para agregar los clientes del postman
listaBoleta.then(async function(response){
    if(response.ok) {
        const Boleta = await response.json();
        console.log('Datos del id boleta obtenidos correctamente:', Boleta);
        
        let options = "";
        Boleta.forEach(Boleta => {
            options += `<option value="${Boleta.id}">${Boleta.IdBoleta}</option>`;
        });
        cboBoleta.innerHTML = options;
        
        console.log('Opciones del id boletageneradas:', options);
    } else {
        console.error('Error al obtener los datos id boleta:', response.statusText);
    }
}).catch(function(error){
    console.error('Error en la solicitud fetch:', error);
}).finally(() => {
    console.log("Terminó el proceso de obtención de id boleta");
});


// listado y funcion para agregar los clientes del postman
listaClientes.then(async function(response){
    if(response.ok) {
        const clientes = await response.json();
        console.log('Datos del cliente obtenidos correctamente:', clientes);
        
        let options = "";
        clientes.forEach(cliente => {
            options += `<option value="${cliente.id}">${cliente.rut}</option>`;
        });
        cboCliente.innerHTML = options;
        
        console.log('Opciones del cliente generadas:', options);
    } else {
        console.error('Error al obtener los datos del cliente:', response.statusText);
    }
}).catch(function(error){
    console.error('Error en la solicitud fetch:', error);
}).finally(() => {
    console.log("Terminó el proceso de obtención de clientes");
});


//productos del postman

listaProductos.then(async function(response){
    if(response.ok) {
        const Productos = await response.json();
        console.log('Producto obtenidos correctamente:', Productos);
        
        let options = "";
        Productos.forEach(Productos => {
            options += `<option value="${Productos.id}">${Productos.tipoProd}</option>`;
        });
        cboProducto.innerHTML = options;
        
        console.log('Opciones producto generadas:', options);
    } else {
        console.error('Error al obtener los productos:', response.statusText);
    }
}).catch(function(error){
    console.error('Error en la solicitud fetch:', error);
}).finally(() => {
    console.log("Terminó el proceso de obtención de productos");
});



// nombre producto 
listaSubProductos.then(async function(response){
    if(response.ok) {
        const Subproductos = await response.json();
        console.log('Producto obtenidos correctamente:', Subproductos);
        
        let options = "";
        Subproductos.forEach(Subproductos => {
            options += `<option value="${Subproductos.id}">${Subproductos.nombre}</option>`;
        });
        cboSubProducto.innerHTML = options;
        
        console.log('Opciones subproducto generadas:', options);
    } else {
        console.error('Error al obtener los subproductos:', response.statusText);
    }
}).catch(function(error){
    console.error('Error en la solicitud fetch:', error);
}).finally(() => {
    console.log("Terminó el proceso de obtención de subproductos");
});

// precio producto 
listaPrecio.then(async function(response){
    if(response.ok) {
        const Precio = await response.json();
        console.log('Precio obtenido correctamente:', Precio);
        
        let options = "";
        Precio.forEach(Precio => {
            options += `<option value="${Precio.id}">${Precio.precio}</option>`;
        });
        txtPrecio.innerHTML = options;
        
        console.log('Opciones de Precio generadas:', options);
    } else {
        console.error('Error al obtener los Precio:', response.statusText);
    }
}).catch(function(error){
    console.error('Error en la solicitud fetch:', error);
}).finally(() => {
    console.log("Terminó el proceso de obtención de precio");
});

// Total boleta
listaTotal.then(async function(response){
    if(response.ok) {
        const Total = await response.json();
        console.log('Total obtenido correctamente:', Total);
        
        let options = "";
        Total.forEach(Total => {
            options += `<option value="${Total.id}">${Total.precio}</option>`;
        });
        txtTotal.innerHTML = options;
        
        console.log('Total generado:', options);
    } else {
        console.error('Error al obtener Total', response.statusText);
    }
}).catch(function(error){
    console.error('Error en la solicitud fetch:', error);
}).finally(() => {
    console.log("Terminó el proceso de obtención de Total");
});