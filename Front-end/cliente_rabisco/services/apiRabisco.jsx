// Importamos a biblioteca Axios
import axios from 'axios'
// Criamos uma instância do Axios com a configuração da baseURL, que é o endereço principal do nosso servidor
const api = axios.create({baseURL: 'http://localhost:5000'})
export async function getProdutos(){
    try {
        const response = await api.get('/produto')
        return response.data
    } catch (error){
        console.error(`Erro ao buscar produtos: ${error.message}`)
    }
}