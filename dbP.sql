--CLIENTE
	--DROP A PROCEDIMIENTOS ALMACENADOS
	go
	IF EXISTS (SELECT * FROM sys.objects WHERE type = 'P' AND name = 'p_postCli')
	DROP PROCEDURE p_postCli

	go
	IF EXISTS (SELECT * FROM sys.objects WHERE type = 'P' AND name = 'p_putCli')
	DROP PROCEDURE p_putCli

	go
	IF EXISTS (SELECT * FROM sys.objects WHERE type = 'P' AND name = 'p_getCli')
	DROP PROCEDURE p_getCli

	go
	IF EXISTS (SELECT * FROM sys.objects WHERE type = 'P' AND name = 'p_getAllCli')
	DROP PROCEDURE p_getAllCli

	go
	IF EXISTS (SELECT * FROM sys.objects WHERE type = 'P' AND name = 'p_deleteCli')
	DROP PROCEDURE p_deleteCli


	--CREACION DE PROCEDIMIENTOS ALMACENADOS

	--POST
	GO
	CREATE PROCEDURE p_postCli(
		@nombre varchar(100),
		@rut varchar(20),
		@telefono varchar(20),
		@direccion varchar(100)
	)
	as
	begin
		insert into cliente(nombreCli,rut,telefono,direccion)
		values
		(
		@nombre,
		@rut,
		@telefono,
		@direccion
		)

	END

	--PUT
	GO
	CREATE PROCEDURE p_putCli(
		@id int,
		@nombre varchar(100),
		@rut varchar(20),
		@telefono varchar(20),
		@direccion varchar(100)
	)
	AS
	BEGIN

		update cliente set 
		nombreCli = @nombre,
		rut = @rut,
		telefono = @telefono,
		direccion = @direccion
		where idCliente = @id

	END

	--GET POR ID
	GO
	CREATE PROCEDURE p_getCli(@id int)
	AS
	BEGIN

		SELECT * FROM cliente WHERE idCliente = @id

	END

	--GET DE TODOS LOS CLIENTES
	GO
	CREATE PROCEDURE p_getAllCli
	AS
	BEGIN

		SELECT * FROM cliente

	END

	--DELETE
	GO
	CREATE PROCEDURE p_deleteCli(@id int)
	AS
	BEGIN

		DELETE FROM cliente WHERE idCliente = @id

	END

--PRODUCTO
	--DROP A PROCEDIMIENTOS ALMACENADOS
	go
	IF EXISTS (SELECT * FROM sys.objects WHERE type = 'P' AND name = 'p_postProd')
	DROP PROCEDURE p_postProd

	go
	IF EXISTS (SELECT * FROM sys.objects WHERE type = 'P' AND name = 'p_putProd')
	DROP PROCEDURE p_putProd

	go
	IF EXISTS (SELECT * FROM sys.objects WHERE type = 'P' AND name = 'p_getProd')
	DROP PROCEDURE p_getProd

	go
	IF EXISTS (SELECT * FROM sys.objects WHERE type = 'P' AND name = 'p_getAllProd')
	DROP PROCEDURE p_getAllProd

	go
	IF EXISTS (SELECT * FROM sys.objects WHERE type = 'P' AND name = 'p_deleteProd')
	DROP PROCEDURE p_deleteProd


	--CREACION DE PROCEDIMIENTOS ALMACENADOS

	--POST
	GO
	CREATE PROCEDURE p_postProd(
		@nombre varchar(100),
		@precio int,
		@marca varchar(20),
		@tipo varchar(100)
	)
	as
	begin
		insert into producto(nombreProd,precio,marca,tipoProd)
		values
		(
		@nombre,
		@precio,
		@marca,
		@tipo
		)

	END

	--PUT
	GO
	CREATE PROCEDURE p_putProd(
		@id int,
		@nombre varchar(100),
		@precio int,
		@marca varchar(20),
		@tipo varchar(100)
	)
	AS
	BEGIN

		update producto set 
		nombreProd = @nombre,
		precio = @precio,
		marca = @marca,
		tipoProd = @tipo
		where idProducto = @id

	END

	--GET POR ID
	GO
	CREATE PROCEDURE p_getProd(@id int)
	AS
	BEGIN

		SELECT * FROM producto WHERE idProducto = @id

	END

	--GET DE TODOS LOS CLIENTES
	GO
	CREATE PROCEDURE p_getAllProd
	AS
	BEGIN

		SELECT * FROM producto

	END

	--DELETE
	GO
	CREATE PROCEDURE p_deleteProd(@id int)
	AS
	BEGIN

		DELETE FROM producto WHERE idProducto = @id

	END

--Boleta

	--DROP A PROCEDIMIENTOS ALMACENADOS 
	go
	IF EXISTS (SELECT * FROM sys.objects WHERE type = 'P' AND name = 'p_postBol')
	DROP PROCEDURE p_postBol

	go
	IF EXISTS (SELECT * FROM sys.objects WHERE type = 'P' AND name = 'p_putBol')
	DROP PROCEDURE p_putBol

	go
	IF EXISTS (SELECT * FROM sys.objects WHERE type = 'P' AND name = 'p_getBol')
	DROP PROCEDURE p_getBol

	go
	IF EXISTS (SELECT * FROM sys.objects WHERE type = 'P' AND name = 'p_getAllBol')
	DROP PROCEDURE p_getAllBol

	go
	IF EXISTS (SELECT * FROM sys.objects WHERE type = 'P' AND name = 'p_deleteBol')
	DROP PROCEDURE p_deleteBol

	--POST
	GO
	CREATE PROCEDURE p_postBol(
		@cantidad int,
		@total int,
		@tipoEntrega varchar(100),
		@fechaBoleta varchar(100),
		@clienteId int,
		@productoId int

	)
	as
	begin
		DECLARE @boletaid INT;
		insert into boleta(cantidad,total,tipoEntrega,fechaBoleta,clienteId,productoId)
		values
		(
		@cantidad,
		@total,
		@tipoEntrega,
		@fechaBoleta,
		@clienteId,
		@productoId
		)

		--Esto guarda la primary key que se creo en el anterior post en la tabla boleta para usarla como foreign key en la tabla pedido
		SET @boletaid = SCOPE_IDENTITY();

		--Se hace un post a pedido
		insert into pedido(estado, boletaId)
		values
		(
		'Procesando compra',
		@boletaid
		)
	END

	--PUT
	GO
	CREATE PROCEDURE p_putBol(
		@id int,
		@cantidad int,
		@total int,
		@tipoEntrega varchar(100)
	)
	AS
	BEGIN

		update boleta set 
		cantidad = @cantidad,
		total = @total,
		tipoEntrega = @tipoEntrega
		where idBoleta = @id

	END

	--GET POR ID
	GO
	CREATE PROCEDURE p_getBol(@id int)
	AS
	BEGIN

		SELECT * FROM boleta WHERE idBoleta = @id

	END

	--GET DE TODOS LOS CLIENTES
	GO
	CREATE PROCEDURE p_getAllBol
	AS
	BEGIN

		SELECT * FROM boleta

	END

	--DELETE
	GO
	CREATE PROCEDURE p_deleteBol(@id int)
	AS
	BEGIN

		DELETE FROM boleta WHERE idBoleta = @id

	END

--Pedido
	
	--DROP A PROCEDIMIENTOS ALMACENADOS 

	go
	IF EXISTS (SELECT * FROM sys.objects WHERE type = 'P' AND name = 'p_putPed')
	DROP PROCEDURE p_putPed

	go
	IF EXISTS (SELECT * FROM sys.objects WHERE type = 'P' AND name = 'p_getPed')
	DROP PROCEDURE p_getPed

	go
	IF EXISTS (SELECT * FROM sys.objects WHERE type = 'P' AND name = 'p_getAllPed')
	DROP PROCEDURE p_getAllPed

	go
	IF EXISTS (SELECT * FROM sys.objects WHERE type = 'P' AND name = 'p_deletePed')
	DROP PROCEDURE p_deletePed

	--PUT
	GO
	CREATE PROCEDURE p_putPed(
		@id int,
		@estado varchar(100)
	)
	AS
	BEGIN

		update pedido set 
		estado = @estado
		where idPedido = @id

	END

	--GET POR ID
	GO
	CREATE PROCEDURE p_getPed(@id int)
	AS
	BEGIN

		SELECT 
			pedido.idPedido,
			cliente.nombreCli,
			pedido.estado,
			boleta.tipoEntrega,
			boleta.fechaBoleta
		FROM pedido
		JOIN boleta ON pedido.idPedido = boleta.idBoleta
		JOIN cliente ON boleta.idBoleta = cliente.idCliente
		WHERE idPedido = @id

	END

	--GET DE TODOS LOS CLIENTES
	GO
	CREATE PROCEDURE p_getAllPed
	AS
	BEGIN

		SELECT 
			pedido.idPedido,
			cliente.nombreCli,
			pedido.estado,
			boleta.tipoEntrega,
			boleta.fechaBoleta
		FROM pedido
		JOIN boleta ON pedido.idPedido = boleta.idBoleta
		JOIN cliente ON boleta.idBoleta = cliente.idCliente

	END

	--DELETE
	GO
	CREATE PROCEDURE p_deletePed(@id int)
	AS
	BEGIN

		DELETE FROM pedido WHERE idPedido = @id

	END