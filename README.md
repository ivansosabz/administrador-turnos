# Gestor de Turnos

Sistema web desarrollado con Django para gestionar la rotación de turnos de cuidado familiar.
Permite que cualquier persona se registre, cree su grupo familiar, agregue responsables y administre
los turnos de manera automatica segun un ciclo de rotacion configurable.

## Tecnologias

- Python / Django
- Bootstrap 5
- SQLite (desarrollo)

---

## Metodologia de trabajo con Git

### Crear una rama desde main

```bash
git checkout main
git pull origin main
git checkout -b feat/nombre-funcionalidad
```

> El comando `checkout -b` crea la rama y se cambia a ella en un solo paso.

### Commit inicial vacio

Al crear una rama nueva se hace un commit vacio para registrar su existencia en el repositorio remoto
desde el principio.

```bash
git commit --allow-empty -m "feat: inicio rama nombre-funcionalidad"
git push origin feat/nombre-funcionalidad
```

### Trabajar en la rama

```bash
git add .
git commit -m "feat: descripcion del cambio"
git push origin feat/nombre-funcionalidad
```

### Pull Request

Se hace un Pull Request unicamente cuando el modulo esta completo y probado.
No se mergea codigo a medias. Cada PR corresponde a una funcionalidad terminada.

```bash
# luego del merge, volver a main y crear la siguiente rama
git checkout main
git pull origin main
git checkout -b feat/siguiente-funcionalidad
```

---

## Prefijos para mensajes de commit

| Prefijo | Uso |
|--------|-----|
| `feat:` | Nueva funcionalidad |
| `fix:` | Correccion de error |
| `refactor:` | Reorganizacion de codigo sin cambiar comportamiento |
| `style:` | Cambios de estilos o formato |
| `docs:` | Cambios en documentacion |

---

## Comandos importantes

### fetch
Descarga los cambios del servidor remoto pero no modifica el codigo local.
Util para ver que cambio antes de integrar.

```bash
git fetch origin
```

### merge
Integra los cambios de otra rama en la rama actual. Es la forma mas segura de mantener
la rama al dia con main.

```bash
git merge origin/main
```

---

## Deshacer cambios

### restore
Descarta cambios locales que todavia no se comitearon. Se usa cuando se edito un archivo
y se quiere volver al estado anterior.

```bash
git restore archivo.py
```

### reset
Mueve el HEAD hacia atras. Solo se usa en la rama local propia, nunca en ramas compartidas.

```bash
git reset --soft HEAD~1   # deshace el ultimo commit pero conserva los cambios
git reset --hard HEAD~1   # deshace el ultimo commit y borra todo
```

### revert
Deshace un commit que ya fue pusheado al remoto. Genera un commit nuevo que anula el anterior.
Se usa cuando el error ya esta en main o en una rama compartida.

```bash
git revert abc1234   # el hash del commit que se quiere anular
```

---

## Notas importantes

- Commitear antes de cambiar de rama para no perder trabajo
- Nunca usar `reset` en ramas compartidas
- Nunca pushear directamente a `main`
- Cada rama representa una funcionalidad o modulo completo

---

## Modulos del sistema

| Modulo | Estado |
|--------|--------|
| Autenticacion (registro, login, logout) | Completado |
| Grupos familiares | Completado |
| Responsables | Completado |
| Ciclos de rotacion | Completado |
| Turnos reales | Pendiente |
