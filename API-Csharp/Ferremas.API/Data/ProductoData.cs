using Ferremas.API.Models;
using System;
using System.Collections.Generic;
using System.Data;
using System.Data.SqlClient;
using System.Linq;
using System.Threading.Tasks;

namespace Ferremas.API.Data
{
    public class ProductoData
    {

        public static bool PostProd(Producto oProducto)
        {
            using (SqlConnection oConexion = new SqlConnection(Conexion.ConexionBD))
            {
                SqlCommand cmd = new SqlCommand("p_postProd", oConexion);
                cmd.CommandType = CommandType.StoredProcedure;
                cmd.Parameters.AddWithValue("@nombre", oProducto.Nombre);
                cmd.Parameters.AddWithValue("@precio", oProducto.Precio);
                cmd.Parameters.AddWithValue("@marca", oProducto.Marca);
                cmd.Parameters.AddWithValue("@tipo", oProducto.TipoProd);
                try
                {
                    oConexion.Open();
                    cmd.ExecuteNonQuery();
                    return true;
                }
                catch (Exception ex)
                {
                    return false;
                }
            }

        }

        public static bool PutProd(int id, Producto oProducto)
        {
            using (SqlConnection oConexion = new SqlConnection(Conexion.ConexionBD))
            {
                SqlCommand cmd = new SqlCommand("p_putProd", oConexion);
                cmd.CommandType = CommandType.StoredProcedure;
                cmd.Parameters.AddWithValue("@id", id);
                cmd.Parameters.AddWithValue("@nombre", oProducto.Nombre);
                cmd.Parameters.AddWithValue("@precio", oProducto.Precio);
                cmd.Parameters.AddWithValue("@marca", oProducto.Marca);
                cmd.Parameters.AddWithValue("@tipo", oProducto.TipoProd);

                try
                {
                    oConexion.Open();
                    cmd.ExecuteNonQuery();
                    return true;
                }
                catch (Exception ex)
                {
                    return false;
                }
            }
        }

        public static List<Producto> GetAllProd()
        {
            List<Producto> oListaProducto = new List<Producto>();
            using (SqlConnection oConexion = new SqlConnection(Conexion.ConexionBD))
            {
                SqlCommand cmd = new SqlCommand("p_getAllProd", oConexion);
                cmd.CommandType = CommandType.StoredProcedure;

                try
                {
                    oConexion.Open();
                    cmd.ExecuteNonQuery();

                    using (SqlDataReader dr = cmd.ExecuteReader())
                    {

                        while (dr.Read())
                        {
                            oListaProducto.Add(new Producto()
                            {
                                Id = Convert.ToInt32(dr["idProducto"]),
                                Nombre = dr["nombreProd"].ToString(),
                                Precio = Convert.ToInt32(dr["precio"]),
                                Marca = dr["marca"].ToString(),
                                TipoProd = dr["tipoProd"].ToString()
                            });
                        }

                    }

                    return oListaProducto;
                }
                catch (Exception ex)
                {
                    return oListaProducto;
                }
            }
        }

        public static Producto GetProd(int id)
        {
            Producto oProducto = new Producto();
            using (SqlConnection oConexion = new SqlConnection(Conexion.ConexionBD))
            {
                SqlCommand cmd = new SqlCommand("p_getProd", oConexion);
                cmd.CommandType = CommandType.StoredProcedure;
                cmd.Parameters.AddWithValue("@id", id);

                try
                {
                    oConexion.Open();
                    cmd.ExecuteNonQuery();

                    using (SqlDataReader dr = cmd.ExecuteReader())
                    {

                        while (dr.Read())
                        {
                            oProducto = new Producto()
                            {
                                Id = Convert.ToInt32(dr["idProducto"]),
                                Nombre = dr["nombreProd"].ToString(),
                                Precio = Convert.ToInt32(dr["precio"]),
                                Marca = dr["marca"].ToString(),
                                TipoProd = dr["tipoProd"].ToString()
                            };
                        }

                    }



                    return oProducto;
                }
                catch (Exception ex)
                {
                    return oProducto;
                }
            }
        }

        public static bool DeleteProd(int id)
        {
            using (SqlConnection oConexion = new SqlConnection(Conexion.ConexionBD))
            {
                SqlCommand cmd = new SqlCommand("p_deleteProd", oConexion);
                cmd.CommandType = CommandType.StoredProcedure;
                cmd.Parameters.AddWithValue("@id", id);

                try
                {
                    oConexion.Open();
                    cmd.ExecuteNonQuery();
                    return true;
                }
                catch (Exception ex)
                {
                    return false;
                }
            }
        }

    }
}
