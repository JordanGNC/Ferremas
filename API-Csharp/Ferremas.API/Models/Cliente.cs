using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Ferremas.API.Models
{
    public class Cliente
    {
        public int Id { get; set; }
        public string Nombre { get; set; }
        public string Rut { get; set; }
        public string Telefono { get; set; }
        public string Direccion { get; set; }
    }
}
