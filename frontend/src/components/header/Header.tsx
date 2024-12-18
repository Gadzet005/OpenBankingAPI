import { observer } from "mobx-react-lite";
import { useGetUser } from "../../public/user";
import { navList, userMenuList } from "./headerList";
import { internal } from "./internal";
import {
  AppBar,
  Avatar,
  Box,
  Container,
  IconButton,
  Link,
  Menu,
  MenuItem,
  Toolbar,
  Tooltip,
  Typography,
} from "@mui/material";
import { Path } from "../../routing/path";
import Ship from "/ship.png";
import { NavItem } from "./NavItem";
import React from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { mochaColors } from "../../public/style/colors";

export const Header = observer(() => {
  const location = useLocation();
  const navigate = useNavigate();

  const user = useGetUser();

  const [activeNavElemIdx, setActiveNavElemIdx] = React.useState(() => -1);
  React.useEffect(() => {
    setActiveNavElemIdx(
      navList.findIndex((item) => location.pathname === item.path),
    );
  }, [location.pathname]);

  const [anchorElUser, setAnchorElUser] = React.useState<null | HTMLElement>(
    null,
  );

  const handleOpenUserMenu = (event: React.MouseEvent<HTMLElement>) => {
    setAnchorElUser(event.currentTarget);
  };

  const handleCloseUserMenu = () => {
    setAnchorElUser(null);
  };

  const navItems = internal
    .filterByType(navList, user.isAuth)
    .map((item, idx) => {
      const { name, path } = item as internal.HeaderLinkItem;
      if (!path) {
        return null;
      }
      return (
        <NavItem
          key={idx}
          name={name}
          path={path}
          isActive={idx == activeNavElemIdx}
          isActiveHandler={() => setActiveNavElemIdx(idx)}
        />
      );
    });

  const userMenuItems = internal
    .filterByType(userMenuList, user.isAuth)
    .map(({ name, path, onClick }, idx) => {
      return (
        <MenuItem
          sx={{
            bgcolor: mochaColors.base,
          }}
          key={idx}
          onClick={() => {
            if (onClick) {
              onClick({ user, navigate });
            }
            if (path) {
              navigate(path);
            }
            handleCloseUserMenu();
          }}
        >
          <Typography sx={{ textAlign: "center" }}>{name}</Typography>
        </MenuItem>
      );
    });

  return (
    <AppBar
      sx={{ mb: 3, bgcolor: mochaColors.mantle }}
      color="transparent"
      position="static"
      enableColorOnDark
    >
      <Container maxWidth="xl">
        <Toolbar
          sx={{ display: "flex", justifyContent: "space-between" }}
          disableGutters
        >
          <Box sx={{ display: "flex", alignItems: "center" }}>
            <Box
              sx={{ height: "64px", width: "64px", mr: 1 }}
              component="img"
              src={Ship}
            />
            <Link
              variant="h6"
              href={Path.homePage}
              sx={{
                mr: 2,
                textDecoration: "none",
                color: mochaColors.text,
              }}
            >
              Тонущий корабль
            </Link>
          </Box>

          <Box
            sx={{
              display: "flex",
              gap: 3,
            }}
          >
            {navItems}
          </Box>

          <Box
            sx={{
              width: { md: "15%" },
              display: "flex",
              justifyContent: "center",
            }}
          >
            <Tooltip title="Пользователь">
              <IconButton onClick={handleOpenUserMenu} sx={{ p: 0 }}>
                <Avatar sx={{ bgcolor: mochaColors.blue }}>
                  {user.email ? user.email[0].toUpperCase() : null}
                </Avatar>
              </IconButton>
            </Tooltip>
            <Menu
              sx={{ mt: "45px" }}
              id="menu-appbar"
              anchorEl={anchorElUser}
              anchorOrigin={{
                vertical: "top",
                horizontal: "center",
              }}
              keepMounted
              transformOrigin={{
                vertical: "top",
                horizontal: "center",
              }}
              open={Boolean(anchorElUser)}
              onClose={handleCloseUserMenu}
            >
              {userMenuItems}
            </Menu>
          </Box>
        </Toolbar>
      </Container>
    </AppBar>
  );
});
