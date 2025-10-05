import React, {useState} from 'react'
import axios from 'axios'

export default function UploadForm(){
  const [file, setFile] = useState(null)
  const [result, setResult] = useState(null)

  const handleSubmit = async (e) =>{
    e.preventDefault()
    if(!file) return
    const fd = new FormData()
    fd.append('file', file)
    const res = await axios.post('/api/predict', fd, { headers: {'Content-Type':'multipart/form-data'} })
    setResult(res.data)
  }

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input type="file" accept=".csv,.fits" onChange={e=>setFile(e.target.files[0])} />
        <button type="submit">Enviar</button>
      </form>
      {result && <pre>{JSON.stringify(result, null, 2)}</pre>}
    </div>
  )
}
