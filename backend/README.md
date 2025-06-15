# SISTEMA DE GESTIÓN DE PRESTAMOS V1.0.0

- Sistema de gestión de prestamos para uso personal.

## 📁 Estructura del proyecto
```text
gestion_prestamos/
├── apps/
│   ├── users/               ← gestión de usuarios y perfiles
│   ├── clientes/            ← información de clientes y sus direcciones
│   ├── prestamos/           ← lógica de creación de préstamos y cronograma
│   ├── pagos/               ← pagos realizados, cuotas, moras
│   ├── parametros/          ← catálogos reutilizables (roles, estados, tipos de pago)
├── manage.py
└── settings/
    ├── base.py
    ├── dev.py
    └── prod.py
```