# Contributing to Calculator Agent

Bu dokümanda, Calculator Agent projesine nasıl katkıda bulunabileceğiniz açıklanmıştır.

## 🎯 Hackathon Context

Bu proje AI Builder Challenge Hackathon için geliştirilmiştir. Hackathon challenge'ı tamamlanmıştır, ancak projeye katkıda bulunmak isteyenler için rehber aşağıdadır.

## 📋 Development Setup

### Gereksinimler
- Python 3.11+
- Git
- Google Gemini API Key

### Kurulum
```bash
# Repository'yi klonlayın
git clone <repository-url>
cd calculator-agent

# Virtual environment oluşturun
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Dependencies yükleyin
pip install -r requirements.txt

# Environment variables ayarlayın
cp .env.example .env
# .env dosyasını düzenleyip API key'inizi ekleyin
```

## 🔧 Development Workflow

### 1. Branch Oluşturma
```bash
# Feature branch oluşturun
git checkout -b feature/your-feature-name

# Bug fix branch
git checkout -b fix/bug-description
```

### 2. Kod Yazma
```python
# Type hints kullanın
def calculate(self, expression: str) -> CalculationResult:
    """
    Hesaplama yapar.
    
    Args:
        expression: Hesaplanacak ifade
        
    Returns:
        CalculationResult objesi
    """
    pass

# Docstring ekleyin (Google style)
# Error handling yapın
# Input validation ekleyin
```

### 3. Testing
```bash
# Testleri çalıştırın
pytest tests/ -v

# Coverage kontrolü
pytest --cov=src --cov-report=html

# Specific test
pytest tests/modules/test_your_module.py -v
```

### 4. Code Quality
```bash
# Linting
pylint src/

# Type checking
mypy src/

# Format checking
black src/ --check

# Auto format
black src/
```

### 5. Commit
```bash
# Staged changes
git add .

# Semantic commit message
git commit -m "feat: add new statistics module"
git commit -m "fix: resolve division by zero in calculus"
git commit -m "docs: update README with new examples"
```

### 6. Push & PR
```bash
# Push to remote
git push origin feature/your-feature-name

# Create Pull Request on GitHub
# PR template'i doldurun
```

## 📝 Commit Message Guidelines

### Format
```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types
- **feat**: Yeni özellik
- **fix**: Bug fix
- **docs**: Dokümantasyon
- **style**: Formatting, semicolons, etc.
- **refactor**: Code refactoring
- **test**: Test ekleme/düzeltme
- **chore**: Build, dependencies, etc.

### Örnekler
```bash
feat(modules): add statistics calculation module

Added new module for statistical calculations including:
- Mean, median, mode
- Standard deviation
- Variance
- Correlation

Closes #123

---

fix(agent): resolve rate limiting issue

Rate limiter was not respecting the period parameter.
Changed calculation to use seconds instead of milliseconds.

Fixes #456

---

docs(README): add API usage examples

Added comprehensive examples for:
- Basic calculations
- Advanced calculus
- Custom module creation
```

## 🧪 Testing Guidelines

### Test Structure
```python
import pytest
from src.modules.your_module import YourModule

@pytest.mark.asyncio
async def test_your_feature(mock_gemini_agent):
    """Test açıklaması"""
    # Arrange
    module = YourModule(mock_gemini_agent)
    input_data = "test input"
    
    # Act
    result = await module.calculate(input_data)
    
    # Assert
    assert result is not None
    assert result.result == expected_value
    assert len(result.steps) > 0
```

### Test Coverage
- **Minimum %80 coverage** hedefleyin
- Edge cases'i test edin
- Error scenarios'ı test edin
- Happy path'i test edin

### Test Naming
```python
# ✅ İyi
def test_calculus_derivative_polynomial():
    pass

def test_basic_math_division_by_zero_raises_error():
    pass

# ❌ Kötü
def test_calc():
    pass

def test_1():
    pass
```

## 📚 Documentation Guidelines

### Docstrings
```python
def complex_function(
    param1: str,
    param2: int,
    optional_param: Optional[float] = None
) -> Dict[str, Any]:
    """
    Kısa bir satırda fonksiyon açıklaması.
    
    Daha detaylı açıklama buraya gelir. Birden fazla
    paragraf olabilir.
    
    Args:
        param1: İlk parametre açıklaması
        param2: İkinci parametre açıklaması
        optional_param: Opsiyonel parametre (default: None)
        
    Returns:
        Dict containing:
            - key1: Açıklama
            - key2: Açıklama
            
    Raises:
        ValueError: Geçersiz input durumunda
        APIError: API çağrısı başarısız olduğunda
        
    Examples:
        >>> result = complex_function("test", 42)
        >>> print(result)
        {'key1': 'value1', 'key2': 'value2'}
    """
    pass
```

### README Updates
Yeni özellik eklerken:
1. README'ye kullanım örneği ekleyin
2. Gerekirse yeni bölüm oluşturun
3. İlgili dokümantasyon linklerini ekleyin

## 🔒 Security Guidelines

### API Keys
```python
# ❌ ASLA yapma
API_KEY = "AIzaSyBj..."

# ✅ Doğru
API_KEY = os.getenv("GEMINI_API_KEY")
```

### Input Validation
```python
# Her kullanıcı input'u validate edin
def sanitize_expression(self, expression: str) -> str:
    # Check forbidden patterns
    for pattern in FORBIDDEN_PATTERNS:
        if pattern in expression:
            raise SecurityViolationError(f"Forbidden: {pattern}")
    return expression
```

### Error Messages
```python
# ❌ Sensitive bilgi leak etme
raise Exception(f"API Key {self.api_key} invalid")

# ✅ Generic message
raise Exception("API authentication failed")
```

## 🎨 Code Style

### Python Style Guide
- **PEP 8** standartlarına uyun
- **Type hints** her yerde kullanın
- **Max line length**: 88 (Black formatter)
- **Imports**: stdlib, third-party, local order

### Variable Naming
```python
# ✅ İyi
calculation_result: CalculationResult
user_input: str
api_response: Dict[str, Any]

# ❌ Kötü
cr: CalculationResult
inp: str
resp: Dict[str, Any]
```

### Function Naming
```python
# ✅ İyi
def calculate_derivative(expression: str) -> float:
    pass

def validate_input(data: str) -> bool:
    pass

# ❌ Kötü
def calc(e: str) -> float:
    pass

def val(d: str) -> bool:
    pass
```

## 🐛 Bug Reports

### Template
```markdown
**Bug Açıklaması**
Net ve kısa bug açıklaması.

**Reproduce Steps**
1. Go to '...'
2. Click on '...'
3. See error

**Beklenen Davranış**
Ne olmasını bekliyordunuz?

**Gerçek Davranış**
Ne oldu?

**Screenshots**
Varsa ekleyin.

**Environment:**
- OS: [e.g. Windows 11]
- Python: [e.g. 3.11.0]
- Version: [e.g. 1.0.0]

**Ek Bilgi**
Başka önemli detaylar.
```

## 🎯 Feature Requests

### Template
```markdown
**Özellik İsteği**
Özelliğin kısa açıklaması.

**Problem**
Hangi problemi çözüyor?

**Önerilen Çözüm**
Nasıl implemente edilmeli?

**Alternatifler**
Düşündüğünüz alternatif çözümler.

**Use Cases**
Kimler kullanacak, nasıl kullanacak?

**Priority**
Low / Medium / High / Critical
```

## 📊 Performance Guidelines

### Benchmarking
```python
import time

def benchmark_calculation():
    start = time.time()
    result = calculate_complex_operation()
    end = time.time()
    
    print(f"Operation took {end - start:.3f}s")
    
# Target: <2s for most calculations
```

### Optimization
- Cache sık kullanılan hesaplamaları
- Async operations paralel çalıştır
- Unnecessary API calls'u önle
- Memory leaks kontrol et

## 🤝 Code Review Checklist

Reviewer olarak:
- [ ] Kod çalışıyor mu?
- [ ] Testler var mı ve geçiyor mu?
- [ ] Dokümantasyon güncel mi?
- [ ] Type hints var mı?
- [ ] Security issues var mı?
- [ ] Performance concerns var mı?
- [ ] Code style uygun mu?
- [ ] Error handling yeterli mi?

## 🏆 Recognition

Katkıda bulunanlar:
- README'de Contributors bölümünde listelenecek
- Önemli katkılar CHANGELOG'da mention edilecek
- GitHub contributors graph'te görünecek

## 📞 İletişim / Contact

**🇹🇷 Türkçe:**
- **Geliştirici**: Cenk ÇETİN
- **E-posta**: dev.cenkcetin@gmail.com
- **GitHub Issues**: Teknik sorular
- **GitHub Discussions**: Genel tartışmalar

**🇬🇧 English:**
- **Developer**: Cenk ÇETİN
- **Email**: dev.cenkcetin@gmail.com
- **GitHub Issues**: Technical questions
- **GitHub Discussions**: General discussions

---

**Hackathon Info:**
- **Organizer**: techcareer.net
- **Instructor**: Berkay KAPLAN
- **Event**: AI Builder Challenge 2025

## 📄 Lisans

Bu projeye katkıda bulunarak, katkınızın proje lisansı altında olmasını kabul edersiniz.

---

**Teşekkürler!** 🙏

Katkılarınız projeyi daha iyi hale getiriyor!
