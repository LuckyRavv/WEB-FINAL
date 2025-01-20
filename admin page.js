document.getElementById('showMoreBtn').addEventListener('click', function() {
    const moreInfo = document.getElementById('moreInfo');
    moreInfo.classList.toggle('hidden');
    
    // ganti tombol lebih banyak atau sedikit
    if (moreInfo.classList.contains('hidden')) {
        this.textContent = 'Admin Online';
    } else {
        this.textContent = 'Tutup';
    }
});