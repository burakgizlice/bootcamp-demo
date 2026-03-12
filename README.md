# 🤖 Robotik Kol ve CI/CD

> CI/CD Bootcamp 2026 — Canlı Demo Projesi

Bir fabrikada yıllardır sorunsuz çalışan bir robotik kol var. Bir gün birisi masayı değiştiriyor ve her şey bozuluyor. Bu proje, CI/CD pipeline'larının neden önemli olduğunu bu hikaye üzerinden anlatıyor.

## Nasıl Çalışır?

1. `src/kol.py` — Robotik kolun tüm hareketleri
2. `tests/test_kol.py` — Kolun güvenlik testleri
3. Her push'ta GitHub Actions testleri çalıştırır
4. Testler geçerse `docs/index.html` GitHub Pages'a deploy edilir

## Demo Akışı

| Adım | Ne Yapıyoruz | Sonuç |
|------|-------------|-------|
| 1 | Kol kodunu yazıyoruz | ✅ Çalışıyor |
| 2 | Testleri ekliyoruz | ✅ Yeşil pipeline |
| 3 | Masa yüksekliğini değiştiriyoruz | ❌ Kırmızı pipeline |
| 4 | Düzeltiyoruz | ✅ Tekrar yeşil |

## Lokal Çalıştırma

```bash
pip install -r requirements.txt
pytest tests/ -v
```

---

**ALKÜ × NEXUS** — CI/CD Bootcamp 2026
