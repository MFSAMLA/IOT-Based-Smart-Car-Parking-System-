// Listen for parking spot changes
function setupRealtimeListeners() {
  const spotsRef = database.ref('data/floor1/sensorData');
  
  spotsRef.on('value', (snapshot) => {
    const data = snapshot.val();
    updateParkingDisplay(data);
  });
}

function updateParkingDisplay(data) {
  document.getElementById('available-spots').textContent = data.availableSpots;
  document.getElementById('reserved-spots').textContent = data.reservedSpots;
  document.getElementById('total-spots').textContent = data.totalSpots;
  
  // Update parking map visualization
  renderParkingMap(data);
}