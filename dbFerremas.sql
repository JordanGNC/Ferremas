--Creacion de tablas
GO 
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'dbo' AND TABLE_NAME = 'cliente')
CREATE TABLE cliente(
	idCliente INT PRIMARY KEY IDENTITY(1,1),
	nombreCli VARCHAR(100),
	rut VARCHAR(20),
	telefono VARCHAR(20),
	direccion VARCHAR(100)
);

GO 
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'dbo' AND TABLE_NAME = 'producto')
CREATE TABLE producto(
	idProducto INT PRIMARY KEY IDENTITY(1,1),
	nombreProd VARCHAR(100),
	precio INT,
	marca VARCHAR(100),
	tipoProd VARCHAR(100)
);

GO 
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'dbo' AND TABLE_NAME = 'boleta')
CREATE TABLE boleta(
	idBoleta INT PRIMARY KEY IDENTITY(1,1),
	cantidad INT,
	total INT,
	tipoEntrega VARCHAR(100),
	fechaBoleta DATE,
	clienteId INT,
	productoId INT,
	FOREIGN KEY(clienteId) REFERENCES cliente(idCliente),
	FOREIGN KEY(productoId) REFERENCES producto(idProducto)
);

GO 
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'dbo' AND TABLE_NAME = 'pedido')
CREATE TABLE pedido(
	idPedido INT PRIMARY KEY IDENTITY(1,1),
	estado VARCHAR(100),
	boletaId INT,
	FOREIGN KEY(boletaId) REFERENCES boleta(idBoleta)
);

--INSERTS

BEGIN TRANSACTION 
	IF NOT EXISTS (SELECT * FROM cliente WHERE cliente.idCliente = '1')
	INSERT INTO cliente VALUES ('Jordan', '123', '1234', 'casa');

	IF NOT EXISTS (SELECT * FROM producto WHERE producto.idProducto = '1')
	INSERT INTO producto VALUES ('Martillo', 20000, 'CAT', 'Herramienta');

	IF NOT EXISTS (SELECT * FROM boleta WHERE boleta.idBoleta = '1')
	INSERT INTO boleta VALUES (1, 20000, 'Despacho a domicilio', '01/12/2024', 1, 1);

	IF NOT EXISTS (SELECT * FROM pedido WHERE pedido.idPedido = '1')
	INSERT INTO pedido VALUES ('En camino', 1);
	
COMMIT TRANSACTION;


--SELECT
GO
SELECT 
	*
FROM pedido 
JOIN boleta ON pedido.idPedido=boleta.idBoleta;

--DROP TABLE pedido,boleta,cliente,producto

SELECT * FROM cliente