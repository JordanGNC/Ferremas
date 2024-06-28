using Ferremas.API.Models;
using System;
using System.Collections.Generic;
using System.Data;
using System.Data.SqlClient;
using System.Linq;
using System.Threading.Tasks;

namespace Ferremas.API.Data
{
    public class ClienteData
    {

        public static bool PostCli(Cliente oCliente)
        {
            using (SqlConnection oConexion = new SqlConnection(Conexion.ConexionBD))
            {
                SqlCommand cmd = new SqlCommand("p_postCli", oConexion);
                cmd.CommandType = CommandType.StoredProcedure;
                cmd.Parameters.AddWithValue("@nombre", oCliente.Nombre);
                cmd.Parameters.AddWithValue("@rut", oCliente.Rut);
                cmd.Parameters.AddWithValue("@telefono", oCliente.Telefono);
                cmd.Parameters.AddWithValue("@direccion", oCliente.Direccion);
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

        public static bool PutCli(int id, Cliente oCliente)
        {
            using (SqlConnection oConexion = new SqlConnection(Conexion.ConexionBD))
            {
                SqlCommand cmd = new SqlCommand("p_putCli", oConexion);
                cmd.CommandType = CommandType.StoredProcedure;
                cmd.Parameters.AddWithValue("@id", id);
                cmd.Parameters.AddWithValue("@nombre", oCliente.Nombre);
                cmd.Parameters.AddWithValue("@rut", oCliente.Rut);
                cmd.Parameters.AddWithValue("@telefono", oCliente.Telefono);
                cmd.Parameters.AddWithValue("@direccion", oCliente.Direccion);

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

        public static List<Cliente> GetAllCli()
        {
            List<Cliente> oListaCliente = new List<Cliente>();
            using (SqlConnection oConexion = new SqlConnection(Conexion.ConexionBD))
            {
                SqlCommand cmd = new SqlCommand("p_getAllCli", oConexion);
                cmd.CommandType = CommandType.StoredProcedure;

                try
                {
                    oConexion.Open();
                    cmd.ExecuteNonQuery();

                    using (SqlDataReader dr = cmd.ExecuteReader())
                    {

                        while (dr.Read())
                        {
                            oListaCliente.Add(new Cliente()
                            {
                                Id = Convert.ToInt32(dr["idCliente"]),
                                Nombre = dr["nombreCli"].ToString(),
                                Rut = dr["rut"].ToString(),
                                Telefono = dr["telefono"].ToString(),
                                Direccion = dr["direccion"].ToString()
                            });
                        }

                    }

                    return oListaCliente;
                }
                catch (Exception ex)
                {
                    return oListaCliente;
                }
            }
        }

        public static Cliente GetCli(int id)
        {
            Cliente oCliente = new Cliente();
            using (SqlConnection oConexion = new SqlConnection(Conexion.ConexionBD))
            {
                SqlCommand cmd = new SqlCommand("p_getCli", oConexion);
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
                            oCliente = new Cliente()
                            {
                                Id = Convert.ToInt32(dr["idCliente"]),
                                Nombre = dr["nombreCli"].ToString(),
                                Rut = dr["rut"].ToString(),
                                Telefono = dr["Telefono"].ToString(),
                                Direccion = dr["direccion"].ToString()
                            };
                        }

                    }



                    return oCliente;
                }
                catch (Exception ex)
                {
                    return oCliente;
                }
            }
        }

        public static bool DeleteCli(int id)
        {
            using (SqlConnection oConexion = new SqlConnection(Conexion.ConexionBD))
            {
                SqlCommand cmd = new SqlCommand("p_deleteCli", oConexion);
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
