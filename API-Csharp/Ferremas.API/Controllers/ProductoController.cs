using Ferremas.API.Data;
using Ferremas.API.Models;
using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

// For more information on enabling Web API for empty projects, visit https://go.microsoft.com/fwlink/?LinkID=397860

namespace Ferremas.API.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class ProductoController : ControllerBase
    {

        private static IList<Producto> lista = new List<Producto>();

        // GET: api/<ProductoController>
        [HttpGet]
        public List<Producto> Get()
        {
            return ProductoData.GetAllProd();
        }

        // GET api/<ProductoController>/5
        [HttpGet("{id}")]
        public Producto Get(int id)
        {
            return ProductoData.GetProd(id);
        }

        // POST api/<ProductoController>
        [HttpPost]
        public bool Post([FromBody] Producto oProducto)
        {
            return ProductoData.PostProd(oProducto);
        }

        // PUT api/<ProductoController>/5
        [HttpPut("{id}")]
        public bool Put(int id, [FromBody] Producto oProducto)
        {
            return ProductoData.PutProd(id, oProducto);
        }

        // DELETE api/<ProductoController>/5
        [HttpDelete("{id}")]
        public bool Delete(int id)
        {
            return ProductoData.DeleteProd(id);
        }
    }
}
