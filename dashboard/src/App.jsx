import { useEffect, useState } from 'react'
import axios from 'axios'
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js'
import { Bar } from 'react-chartjs-2'

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
)

function App() {
  const [leaderboard, setLeaderboard] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    // In a real environment, this would point to the gh-pages leaderboard.json
    // For development, we might mock it or point to the raw URL
    const fetchLeaderboard = async () => {
      try {
        const response = await axios.get(`${import.meta.env.BASE_URL}leaderboard.json`)
        setLeaderboard(response.data.leaderboard || [])
        setLoading(false)
      } catch (err) {
        // Fallback for development if file not found locally
        console.warn("Could not load from leaderboard.json, using mock data", err)
        setLeaderboard([
          { rank: "1", name: "Sachin", domain: "Coder", nation: "India", points: "1000" },
          { rank: "2", name: "Jane", domain: "Designer", nation: "UK", points: "950" }
        ])
        setLoading(false)
      }
    }
    fetchLeaderboard()
  }, [])

  if (loading) return <div style={{ padding: '20px' }}>Loading...</div>

  const chartData = {
    labels: leaderboard.map(p => p.name),
    datasets: [
      {
        label: 'Points',
        data: leaderboard.map(p => parseInt(p.points, 10)),
        backgroundColor: 'rgba(53, 162, 235, 0.5)',
      },
    ],
  }

  const chartOptions = {
    responsive: true,
    plugins: {
      legend: { position: 'top' },
      title: { display: true, text: 'μFIFA 2026 Leaderboard' },
    },
  }

  return (
    <div style={{ fontFamily: 'sans-serif', padding: '20px', maxWidth: '1000px', margin: '0 auto' }}>
      <h1 style={{ textAlign: 'center', color: '#333' }}>μFIFA 2026 Tournament Dashboard</h1>
      
      <div style={{ marginBottom: '40px' }}>
        <Bar options={chartOptions} data={chartData} />
      </div>

      <h2>Current Standings</h2>
      <table style={{ width: '100%', borderCollapse: 'collapse', marginTop: '20px' }}>
        <thead>
          <tr style={{ backgroundColor: '#f4f4f4', borderBottom: '2px solid #ddd' }}>
            <th style={{ padding: '10px', textAlign: 'left' }}>Rank</th>
            <th style={{ padding: '10px', textAlign: 'left' }}>Name</th>
            <th style={{ padding: '10px', textAlign: 'left' }}>Domain</th>
            <th style={{ padding: '10px', textAlign: 'left' }}>Nation</th>
            <th style={{ padding: '10px', textAlign: 'left' }}>Points</th>
          </tr>
        </thead>
        <tbody>
          {leaderboard.map((player, idx) => (
            <tr key={idx} style={{ borderBottom: '1px solid #eee' }}>
              <td style={{ padding: '10px' }}>{player.rank}</td>
              <td style={{ padding: '10px' }}>{player.name}</td>
              <td style={{ padding: '10px' }}>{player.domain}</td>
              <td style={{ padding: '10px' }}>{player.nation}</td>
              <td style={{ padding: '10px' }}>{player.points}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}

export default App
