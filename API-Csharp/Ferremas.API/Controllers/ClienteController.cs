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
    public class ClienteController : ControllerBase
    {
        // GET: api/<ClienteController>
        [HttpGet]
        public List<Cliente> Get()
        {
            return ClienteData.GetAllCli();
        }

        // GET api/<ClienteController>/5
        [HttpGet("{id}")]
        public Cliente Get(int id)
        {
            return ClienteData.GetCli(id);
        }

        // POST api/<ClienteController>
        [HttpPost]
        public bool Post([FromBody] Cliente oCliente)
        {
            return ClienteData.PostCli(oCliente);
        }

        // PUT api/<ClienteController>/5
        [HttpPut("{id}")]
        public bool Put(int id, [FromBody] Cliente oCliente)
        {
            return ClienteData.PutCli(id, oCliente);
        }

        // DELETE api/<ClienteController>/5
        [HttpDelete("{id}")]
        public bool Delete(int id)
        {
            return ClienteData.DeleteCli(id);
        }
    }
}
