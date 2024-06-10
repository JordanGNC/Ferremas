using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Ferremas.API.Models
{
    public class Producto
    {
        public int Id { get; set; }
        public string Nombre { get; set; }
        public int Precio { get; set; }
        public string Marca { get; set; }
        public string TipoProd { get; set; }
        public string Stock { get; set; }
    }
}
