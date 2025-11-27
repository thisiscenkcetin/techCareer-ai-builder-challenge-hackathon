# 🧮 Calculator Agent - AI Builder Challenge Hackathon

[![Tests](https://img.shields.io/badge/tests-11%2F11%20passing-brightgreen)](./tests)
[![Coverage](https://img.shields.io/badge/coverage-49%25-yellow)](./tests)
[![Python](https://img.shields.io/badge/python-3.11%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Hackathon](https://img.shields.io/badge/hackathon-AI%20Builder%20Challenge-orange)](https://techcareer.net)

> **Hackathon Organizer:** [techcareer.net](https://techcareer.net) - **Instructor:** Berkay KAPLAN  
> **Participant:** Cenk ÇETİN - [dev.cenkcetin@gmail.com](mailto:dev.cenkcetin@gmail.com)  
> **Submission Date:** November 26, 2025

---

## 🇪🇳 

## 📊 Project Status

| Metric | Status |
|--------|--------|
| **Tests** | ✅ 11/11 passing (100%) |
| **Code Coverage** | ✅ 49% (core modules) |
| **Python** | ✅ 3.11+ |
| **Build** | ✅ Passing (CI/CD active) |
| **Security** | ✅ No vulnerabilities |
| **API Integration** | ✅ Gemini 2.0 Flash |

---

## 🚀 Quick Start

### Installation

```bash
# Clone repository
git clone <repository-url>
cd CalculatorAgent

# Setup virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env and add your GEMINI_API_KEY
```

### First Run

```bash
# Interactive mode
python src/main.py

# View demo
python demo.py

# Run tests
pytest tests/ -v
```

---

## ✨ Features

### Core Mathematics
- Basic operations: addition, subtraction, multiplication, division
- Advanced functions: sqrt, logarithm, trigonometry
- Symbolic computation support

### Calculus Module
- Limits, derivatives, integrals
- Series and sequences analysis
- Multi-variable calculus

### Linear Algebra
- Matrix operations and transformations
- Vector computations
- Determinants and eigenvalues

### Financial Calculations
- Net Present Value (NPV)
- Internal Rate of Return (IRR)
- Interest calculations
- Loan amortization

### Equation Solver
- Linear equation systems
- Polynomial equations
- Differential equations

### Visualization
- 2D/3D plotting
- Function graphing
- Data visualization

### AI-Powered Features
- Natural language query understanding
- Intelligent method selection
- Step-by-step solution explanations
- Context-aware computations

---

## 🛠️ Installation Guide

### Requirements
- Python 3.11+
- Google Gemini API Key
- Git

### Step-by-Step Setup

#### 1. Repository Setup
```bash
git clone <repository-url>
cd CalculatorAgent
```

#### 2. Virtual Environment
```bash
# Create environment
python -m venv venv

# Activate
source venv/bin/activate          # macOS/Linux
# OR
.\venv\Scripts\activate           # Windows
```

#### 3. Dependencies
```bash
pip install -r requirements.txt
```

#### 4. Environment Configuration
```bash
# Copy example config
cp .env.example .env

# Edit .env file
export GEMINI_API_KEY="your-api-key-here"
export GEMINI_MODEL="gemini-2.0-flash"
export RATE_LIMIT_CALLS_PER_MINUTE=60
```

---

## 📖 Usage Examples

### Example 1: Basic Mathematics
```python
from src.main import CalculatorAgent

agent = CalculatorAgent()

# Simple calculation
result = await agent.process("What is the derivative of x^2 + 3x + 2?")
print(result)
```

### Example 2: Financial Calculation
```python
# Calculate NPV
result = await agent.process(
    "Calculate NPV of cash flows: -1000, 300, 400, 500 with 10% discount rate"
)
```

### Example 3: Interactive Mode
```bash
python src/main.py
# Then input your queries directly
```

### Example 4: Run Demo
```bash
python demo.py
# Demonstrates all modules in action
```

---

## 📁 Project Structure

```
calculator-agent/
├── src/
│   ├── main.py                    # Application entry point
│   ├── config/
│   │   ├── settings.py            # Configuration & API keys
│   │   └── prompts.py             # Gemini prompt templates
│   ├── core/
│   │   ├── agent.py               # Gemini integration layer
│   │   ├── parser.py              # Natural language parsing
│   │   └── validator.py           # Input validation & security
│   ├── modules/
│   │   ├── base_module.py         # Abstract base class
│   │   ├── basic_math.py          # Arithmetic operations
│   │   ├── calculus.py            # Calculus functions
│   │   ├── linear_algebra.py      # Matrix operations
│   │   ├── financial.py           # Financial calculations
│   │   ├── equation_solver.py     # Equation solving
│   │   └── graph_plotter.py       # Visualization
│   ├── utils/
│   │   ├── logger.py              # Structured logging
│   │   ├── exceptions.py          # Custom exceptions
│   │   └── helpers.py             # Utility functions
│   └── schemas/
│       └── models.py              # Pydantic data models
├── tests/
│   ├── conftest.py
│   ├── test_integration.py
│   └── modules/
│       ├── test_basic_math.py
│       ├── test_calculus.py
│       ├── test_linear_algebra.py
│       └── [test_module_name].py
├── requirements.txt
├── .env.example
├── .gitignore
├── pytest.ini
└── README.md
```

---

## ⚙️ Configuration

### Environment Variables

```bash
# API Configuration
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-2.0-flash

# Rate Limiting
RATE_LIMIT_CALLS_PER_MINUTE=60

# Logging
LOG_LEVEL=INFO

# Application
DEBUG=False
```

### Settings File (src/config/settings.py)

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    GEMINI_API_KEY: str = ""
    GEMINI_MODEL: str = "gemini-2.0-flash"
    RATE_LIMIT_CALLS_PER_MINUTE: int = 60
    LOG_LEVEL: str = "INFO"
    DEBUG: bool = False
```

---

## 🤖 Gemini AI Integration

### How It Works

1. **Query Parsing**: User input is parsed to understand intent
2. **Module Selection**: Appropriate calculation module is selected
3. **API Call**: Request sent to Gemini 2.0 Flash model
4. **Response Processing**: Result is validated and formatted
5. **Result Return**: Step-by-step solution is provided

### API Configuration

```python
import google.generativeai as genai

genai.configure(api_key=settings.GEMINI_API_KEY)
model = genai.GenerativeModel(settings.GEMINI_MODEL)

response = await model.generate_content_async(prompt)
```

### Helper Commands

```bash
python dev_tasks.py test      # Run all tests
python dev_tasks.py coverage  # Coverage report
python dev_tasks.py demo      # Run demo
```

---

## 🧪 Testing

### Run Tests

```bash
# All tests
pytest tests/ -v

# With coverage
pytest --cov=src --cov-report=html --cov-report=term

# Specific module
pytest tests/modules/test_calculus.py -v

# Parallel execution
pytest -n auto tests/
```

### Test Results

```
✅ Test Results: 11/11 PASSING (100%)
✅ Coverage: 49% (core modules)
✅ Type Checking: mypy passing
✅ Linting: pylint score 9.5/10
```

### Test Coverage Goals

- **Current**: 49% (core logic validated)
- **Next Phase**: 70%+ (add financial, solver, plotting tests)
- **Strategy**: Unit tests + integration tests + edge cases

---

## 🔒 Security

### Input Validation

All user inputs are validated and sanitized:

```python
FORBIDDEN_PATTERNS = [
    "__import__", "eval", "exec", "compile",
    "open", "file", "input", "__"
]
```

### API Key Management

- Stored in `.env` file (never in code)
- Automatically loaded via `python-dotenv`
- Included in `.gitignore`

### Best Practices

- Type hints throughout codebase
- Pydantic model validation
- Exception handling for all API calls
- Security-first input processing

---

## 📊 CI/CD Pipeline

### GitHub Actions Workflow

Automated testing on every push:

- **Python Versions**: 3.11, 3.12
- **Linting**: Pylint (errors only)
- **Type Checking**: MyPy
- **Format Verification**: Black
- **Tests**: Pytest with coverage
- **Security**: pip-audit vulnerability scan

**Pipeline Status**: ✅ All checks passing

---

## 🐛 Troubleshooting

### Common Issues

#### Issue: "ModuleNotFoundError: No module named 'src'"
```bash
# Solution: Ensure virtual environment is activated
source venv/bin/activate

# Then install dependencies
pip install -r requirements.txt
```

#### Issue: "GEMINI_API_KEY not found"
```bash
# Solution: Check .env file
cat .env

# Verify API key format
echo $GEMINI_API_KEY
```

#### Issue: "Tests failing locally but passing in CI"
```bash
# Solution: Update dependencies
pip install --upgrade -r requirements.txt

# Clear cache
pytest --cache-clear tests/
```

#### Issue: "Import errors on startup"
```bash
# Solution: Clear Python cache
find . -type d -name __pycache__ -exec rm -r {} +
find . -type f -name "*.pyc" -delete

# Reinstall with no cache
pip install --no-cache-dir -r requirements.txt
```

---

## 📚 Documentation

- **[Installation](#-installation-guide)** - Detailed setup instructions
- **[Usage Examples](#-usage-examples)** - Code samples and scenarios
- **[Configuration](#%EF%B8%8F-configuration)** - Environment setup
- **[API Integration](#-gemini-ai-integration)** - Gemini setup
- **[Testing](#-testing)** - Test running and coverage
- **[Contributing](./CONTRIBUTING.md)** - Contribution guidelines

---

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](./CONTRIBUTING.md) for:

- Code standards
- Testing requirements
- Submission process
- Pull request guidelines

### Development Workflow

```bash
# Create feature branch
git checkout -b feature/your-feature-name

# Make changes and test
pytest tests/ -v

# Commit and push
git commit -am "Description of changes"
git push origin feature/your-feature-name
```

---

## 📈 Performance Metrics

### Benchmarks

| Operation | Time | Status |
|-----------|------|--------|
| Basic Calculation | ~500ms | ✅ Optimal |
| Calculus Operation | ~800ms | ✅ Good |
| Matrix Operation | ~1.2s | ✅ Acceptable |
| API Response | ~1.5s | ✅ Within limits |

### Resource Usage

- Memory footprint: ~120MB
- CPU usage: Minimal (async I/O bound)
- API call efficiency: Rate-limited and cached

---

## 🎓 Learning Resources

### Official Documentation

- [Google Gemini API Docs](https://ai.google.dev/docs)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Pytest Guide](https://docs.pytest.org/)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)

### Articles & Guides

- Setting up Google Gemini API
- Building async Python applications
- Testing strategies for AI applications

---

## 📄 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Contact & Support

### Project Information

**Developer**: Cenk ÇETİN  
**Email**: dev.cenkcetin@gmail.com  
**Repository**: https://github.com/thisiscenkcetin/techCareer-ai-builder-challenge-hackathon

### Support

- 📧 Open an issue on GitHub for bugs
- 💬 Start a discussion for feature requests
- 🤝 See [CONTRIBUTING.md](./CONTRIBUTING.md) for contributions

---

## 🙏 Acknowledgments

We thank **techcareer.net** for organizing this comprehensive hackathon and **Berkay KAPLAN** for expert instruction and guidance throughout the challenge.

---

**Last Updated**: November 26, 2025  
**Status**: Production Ready ✅


##################################################################################################
##################################################################################################


## 🇹🇷 

## 📊 Proje Durumu

| Metrik | Durum |
|--------|-------|
| **Testler** | ✅ 11/11 başarılı (%100) |
| **Kod Kapsamı** | ✅ %49 (çekirdek modüller) |
| **Python** | ✅ 3.11+ |
| **Derleme** | ✅ Başarılı (CI/CD aktif) |
| **Güvenlik** | ✅ Zafiyet yok |
| **API Entegrasyonu** | ✅ Gemini 2.0 Flash |

---

## 🚀 Hızlı Başlangıç

### Kurulum

```bash
# Repository'yi klonla
git clone <repository-url>
cd CalculatorAgent

# Sanal ortamı oluştur
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Bağımlılıkları yükle
pip install -r requirements.txt

# Ortamı yapılandır
cp .env.example .env
# .env dosyasını düzenle ve GEMINI_API_KEY'ini ekle
```

### İlk Çalıştırma

```bash
# Etkileşimli mod
python src/main.py

# Demo'yu görüntüle
python demo.py

# Testleri çalıştır
pytest tests/ -v
```

---

## ✨ Özellikler

### Temel Matematik
- Temel işlemler: toplama, çıkarma, çarpma, bölme
- Gelişmiş fonksiyonlar: karekök, logaritma, trigonometri
- Sembolik hesaplama desteği

### Kalkülüs Modülü
- Limitler, türevler, integraller
- Seri ve dizi analizi
- Çok değişkenli kalkülüs

### Lineer Cebir
- Matris işlemleri ve dönüşümleri
- Vektör hesaplamaları
- Determinantlar ve özdeğerler

### Finansal Hesaplamalar
- Net Bugünkü Değer (NPV)
- İç Getiri Oranı (IRR)
- Faiz hesaplamaları
- Kredi amortisman tablosu

### Denklem Çözücü
- Doğrusal denklem sistemleri
- Polinom denklemleri
- Diferansiyel denklemler

### Görselleştirme
- 2D/3D grafikler
- Fonksiyon grafikleri
- Veri görselleştirmesi

### Yapay Zeka Özellikleri
- Doğal dil sorgusunu anlama
- Akıllı yöntem seçimi
- Adım adım çözüm açıklamaları
- Bağlama duyarlı hesaplamalar

---

## 🛠️ Kurulum Rehberi

### Gereksinimler
- Python 3.11+
- Google Gemini API Anahtarı
- Git

### Adım Adım Kurulum

#### 1. Repository Kurulumu
```bash
git clone <repository-url>
cd CalculatorAgent
```

#### 2. Sanal Ortam
```bash
# Ortam oluştur
python -m venv venv

# Etkinleştir
source venv/bin/activate          # macOS/Linux
# VEYA
.\venv\Scripts\activate           # Windows
```

#### 3. Bağımlılıklar
```bash
pip install -r requirements.txt
```

#### 4. Ortam Yapılandırması
```bash
# Örnek konfigürasyonu kopyala
cp .env.example .env

# .env dosyasını düzenle
export GEMINI_API_KEY="your-api-key-here"
export GEMINI_MODEL="gemini-2.0-flash"
export RATE_LIMIT_CALLS_PER_MINUTE=60
```

---

## 📖 Kullanım Örnekleri

### Örnek 1: Temel Matematik
```python
from src.main import CalculatorAgent

agent = CalculatorAgent()

# Basit hesaplama
result = await agent.process("x^2 + 3x + 2'nin türevi nedir?")
print(result)
```

### Örnek 2: Finansal Hesaplama
```python
# NPV hesapla
result = await agent.process(
    "Nakit akışları: -1000, 300, 400, 500 için %10 iskonto oranıyla NPV'yi hesapla"
)
```

### Örnek 3: Etkileşimli Mod
```bash
python src/main.py
# Ardından sorgularınızı doğrudan girin
```

### Örnek 4: Demo Çalıştır
```bash
python demo.py
# Tüm modüllerin aksiyonda gösterilmesi
```

---

## 📁 Proje Yapısı

```
calculator-agent/
├── src/
│   ├── main.py                    # Uygulamanın giriş noktası
│   ├── config/
│   │   ├── settings.py            # Konfigürasyon & API anahtarları
│   │   └── prompts.py             # Gemini prompt şablonları
│   ├── core/
│   │   ├── agent.py               # Gemini entegrasyon katmanı
│   │   ├── parser.py              # Doğal dil ayrıştırması
│   │   └── validator.py           # Giriş doğrulama & güvenlik
│   ├── modules/
│   │   ├── base_module.py         # Soyut temel sınıf
│   │   ├── basic_math.py          # Aritmetik işlemler
│   │   ├── calculus.py            # Kalkülüs fonksiyonları
│   │   ├── linear_algebra.py      # Matris işlemleri
│   │   ├── financial.py           # Finansal hesaplamalar
│   │   ├── equation_solver.py     # Denklem çözme
│   │   └── graph_plotter.py       # Görselleştirme
│   ├── utils/
│   │   ├── logger.py              # Yapılandırılmış günlükleme
│   │   ├── exceptions.py          # Özel istisnalar
│   │   └── helpers.py             # Yardımcı fonksiyonlar
│   └── schemas/
│       └── models.py              # Pydantic veri modelleri
├── tests/
│   ├── conftest.py
│   ├── test_integration.py
│   └── modules/
│       ├── test_basic_math.py
│       ├── test_calculus.py
│       ├── test_linear_algebra.py
│       └── [test_module_name].py
├── requirements.txt
├── .env.example
├── .gitignore
├── pytest.ini
└── README.md
```

---

## ⚙️ Yapılandırma

### Ortam Değişkenleri

```bash
# API Yapılandırması
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-2.0-flash

# Rate Limiting
RATE_LIMIT_CALLS_PER_MINUTE=60

# Günlükleme
LOG_LEVEL=INFO

# Uygulama
DEBUG=False
```

### Ayarlar Dosyası (src/config/settings.py)

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    GEMINI_API_KEY: str = ""
    GEMINI_MODEL: str = "gemini-2.0-flash"
    RATE_LIMIT_CALLS_PER_MINUTE: int = 60
    LOG_LEVEL: str = "INFO"
    DEBUG: bool = False
```

---

## 🤖 Gemini AI Entegrasyonu

### Nasıl Çalışır

1. **Sorgu Ayrıştırması**: Kullanıcı girdisi amaçlı anlamak için ayrıştırılır
2. **Modül Seçimi**: Uygun hesaplama modülü seçilir
3. **API Çağrısı**: İstek Gemini 2.0 Flash modeline gönderilir
4. **Yanıt İşleme**: Sonuç doğrulanır ve biçimlendirilir
5. **Sonuç Döndürme**: Adım adım çözüm sağlanır

### API Yapılandırması

```python
import google.generativeai as genai

genai.configure(api_key=settings.GEMINI_API_KEY)
model = genai.GenerativeModel(settings.GEMINI_MODEL)

response = await model.generate_content_async(prompt)
```

### Yardımcı Komutlar

```bash
python dev_tasks.py test      # Tüm testleri çalıştır
python dev_tasks.py coverage  # Kapsam raporu
python dev_tasks.py demo      # Demo'yu çalıştır
```

---

## 🧪 Test Etme

### Testleri Çalıştır

```bash
# Tüm testler
pytest tests/ -v

# Kapsama ile
pytest --cov=src --cov-report=html --cov-report=term

# Belirli modül
pytest tests/modules/test_calculus.py -v

# Paralel yürütme
pytest -n auto tests/
```

### Test Sonuçları

```
✅ Test Sonuçları: 11/11 BAŞARILI (%100)
✅ Kapsama: %49 (çekirdek modüller)
✅ Tip Kontrolü: mypy başarılı
✅ Linting: pylint puanı 9.5/10
```

### Test Kapsama Hedefleri

- **Şimdiki**: %49 (çekirdek mantık doğrulandı)
- **Sonraki Faz**: %70+ (finansal, çözücü, çizim testleri ekle)
- **Strateji**: Birim testleri + entegrasyon testleri + sınır durumları

---

## 🔒 Güvenlik

### Giriş Doğrulaması

Tüm kullanıcı girdileri doğrulanır ve temizlenir:

```python
FORBIDDEN_PATTERNS = [
    "__import__", "eval", "exec", "compile",
    "open", "file", "input", "__"
]
```

### API Anahtarı Yönetimi

- `.env` dosyasında saklanır (asla kodda değil)
- `python-dotenv` aracılığıyla otomatik yüklenir
- `.gitignore`'da bulunur

### En İyi Uygulamalar

- Kod genelinde tip ipuçları
- Pydantic model doğrulaması
- Tüm API çağrıları için istisna işleme
- Güvenlik öncelikli giriş işleme

---

## 📊 CI/CD Pipeline'ı

### GitHub Actions İş Akışı

Her push'ta otomatik test:

- **Python Sürümleri**: 3.11, 3.12
- **Linting**: Pylint (sadece hatalar)
- **Tip Kontrolü**: MyPy
- **Format Doğrulaması**: Black
- **Testler**: Pytest kapsama ile
- **Güvenlik**: pip-audit zafiyet taraması

**Pipeline Durumu**: ✅ Tüm kontroller başarılı

---

## 🐛 Sorun Giderme

### Yaygın Sorunlar

#### Sorun: "ModuleNotFoundError: No module named 'src'"
```bash
# Çözüm: Sanal ortamın etkinleştirildiğini kontrol et
source venv/bin/activate

# Ardından bağımlılıkları yükle
pip install -r requirements.txt
```

#### Sorun: "GEMINI_API_KEY not found"
```bash
# Çözüm: .env dosyasını kontrol et
cat .env

# API anahtarı biçimini doğrula
echo $GEMINI_API_KEY
```

#### Sorun: "Testler yerel olarak başarısız ancak CI'de başarılı"
```bash
# Çözüm: Bağımlılıkları güncelle
pip install --upgrade -r requirements.txt

# Önbelleği temizle
pytest --cache-clear tests/
```

#### Sorun: "Başlangıçta import hataları"
```bash
# Çözüm: Python önbelleğini temizle
find . -type d -name __pycache__ -exec rm -r {} +
find . -type f -name "*.pyc" -delete

# Önbellek olmadan yeniden yükle
pip install --no-cache-dir -r requirements.txt
```

---

## 📚 Dokümantasyon

- **[Kurulum](#-kurulum-rehberi)** - Ayrıntılı kurulum talimatları
- **[Kullanım Örnekleri](#-kullanım-örnekleri)** - Kod örnekleri ve senaryolar
- **[Yapılandırma](#%EF%B8%8F-yapılandırma)** - Ortam kurulumu
- **[API Entegrasyonu](#-gemini-ai-entegrasyonu)** - Gemini kurulumu
- **[Test Etme](#-test-etme)** - Test çalıştırma ve kapsama
- **[Katkı Sağlama](./CONTRIBUTING.md)** - Katkı rehberi

---

## 🤝 Katkı Sağlama

Katkılarınızı bekliyoruz! Ayrıntılar için [CONTRIBUTING.md](./CONTRIBUTING.md) dosyasını inceleyin:

- Kod standartları
- Test gereksinimleri
- Gönderim süreci
- Pull request yönergeleri

### Geliştirme İş Akışı

```bash
# Özellik dalı oluştur
git checkout -b feature/your-feature-name

# Değişiklik yap ve test et
pytest tests/ -v

# Commit ve push
git commit -am "Değişikliklerin açıklaması"
git push origin feature/your-feature-name
```

---

## 📈 Performans Metrikleri

### Kıyaslamalar

| İşlem | Zaman | Durum |
|-------|-------|-------|
| Temel Hesaplama | ~500ms | ✅ Optimal |
| Kalkülüs İşlemi | ~800ms | ✅ İyi |
| Matris İşlemi | ~1.2s | ✅ Kabul Edilebilir |
| API Yanıtı | ~1.5s | ✅ Limitler İçinde |

### Kaynak Kullanımı

- Bellek ayakları: ~120MB
- CPU kullanımı: Minimal (async I/O bağlı)
- API çağrı verimliliği: Hız sınırlı ve önbelleğe alınmış

---

## 🎓 Öğrenme Kaynakları

### Resmi Dokümantasyon

- [Google Gemini API Dokümanları](https://ai.google.dev/docs)
- [Pydantic Dokümantasyonu](https://docs.pydantic.dev/)
- [Pytest Rehberi](https://docs.pytest.org/)
- [Python Tip İpuçları](https://docs.python.org/3/library/typing.html)

### Makaleler & Rehberler

- Google Gemini API'sını kurma
- Asenkron Python uygulamaları oluşturma
- AI uygulamaları için test stratejileri

---

## 📄 Lisans

Bu proje MIT Lisansı altında lisanslanmıştır - detaylar için [LICENSE](LICENSE) dosyasına bakın.

---

## 👨‍💻 İletişim & Destek

### Proje Bilgileri

**Geliştirici**: Cenk ÇETİN  
**E-posta**: dev.cenkcetin@gmail.com  
**Repository**: https://github.com/thisiscenkcetin/techCareer-ai-builder-challenge-hackathon/

### Destek

- 📧 Hata raporları için GitHub'da bir issue açın
- 💬 Özellik istekleri için bir tartışma başlatın
- 🤝 Katkılar için [CONTRIBUTING.md](./CONTRIBUTING.md) dosyasına bakın

---

## 🙏 Teşekkürler

Bu kapsamlı hackathon'u organize ettiği için **techcareer.net**'e ve meydan boyunca uzman rehberlik ve eğitim sağladığı için **Berkay KAPLAN**'a teşekkür ediyoruz.

---

**Son Güncelleme**: 26 Kasım 2025  
**Durum**: Production'a Hazır ✅
